// Endpoint de contacto y copia de informe al lead (Resend)
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { nombre, email, telefono, pais, mensaje, empresa_web, copiaAlLead } =
    req.body || {};

  // Honeypot: si el campo oculto viene completo, es un bot
  if (empresa_web) {
    return res.status(200).json({ message: "OK" });
  }

  // Validación básica
  if (!nombre || !email || !mensaje) {
    return res.status(400).json({ message: "Faltan campos obligatorios" });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ message: "Email inválido" });
  }
  const clean = (s) =>
    String(s || "").slice(0, 2000).replace(/</g, "&lt;").replace(/>/g, "&gt;");

  const { error } = await resend.emails.send({
    from: "Gen+ Igualdad <contacto@genigualdad.com>",
    to: ["larod63@gmail.com", "genigualdad@gmail.com"],
    reply_to: email,
    subject: `Consulta web de ${clean(nombre)}${pais ? " · " + clean(pais) : ""}`,
    html: `
      <img src="https://www.genigualdad.com/img/logo-horizontal.png" alt="GEN+ Igualdad" width="200" style="width:200px;max-width:55%;height:auto;margin-bottom:14px">
      <h2 style="color:#2d1b4e">Nueva consulta desde genigualdad.com</h2>
      <p><strong>Nombre:</strong> ${clean(nombre)}</p>
      <p><strong>Email:</strong> ${clean(email)}</p>
      <p><strong>Teléfono:</strong> ${clean(telefono) || "—"}</p>
      <p><strong>País:</strong> ${clean(pais) || "—"}</p>
      <p><strong>Mensaje:</strong></p>
      <p style="background:#f8f5ff;border-left:4px solid #5bc4bf;padding:14px;white-space:pre-wrap">${clean(mensaje)}</p>
      <p style="color:#888;font-size:12px">Podés responder directamente a este email: la respuesta le llegará a ${clean(email)}.</p>
    `,
  });

  if (error) {
    return res.status(500).json({ message: "Error al enviar el mensaje" });
  }

  // Copia al lead: si la persona pidió recibir su informe, se lo enviamos.
  if (copiaAlLead) {
    try {
      await resend.emails.send({
        from: "Gen+ Igualdad <contacto@genigualdad.com>",
        to: [email],
        reply_to: "contacto@genigualdad.com",
        subject: "Tu informe de brecha salarial · Gen+ Igualdad",
        html: `
          <div style="font-family:Arial,sans-serif;color:#221c2e;max-width:560px">
            <img src="https://www.genigualdad.com/img/logo-horizontal.png" alt="GEN+ Igualdad" width="220" style="width:220px;max-width:60%;height:auto;margin-bottom:18px">
            <h2 style="color:#2d1b4e">Hola ${clean(nombre)}, acá está tu informe</h2>
            <p>Gracias por usar la calculadora de brecha salarial de Gen+ Igualdad. Este es el resultado que generaste:</p>
            <div style="background:#f8f5ff;border-left:4px solid #5bc4bf;padding:16px;white-space:pre-wrap;font-size:15px">${clean(mensaje)}</div>
            <p style="margin-top:20px">Si la brecha te dio media o alta, podemos ayudarte con la auditoría retributiva completa: diagnóstico, valoración de puestos y plan de actuación. La primera consulta es sin costo.</p>
            <p><a href="https://www.genigualdad.com/contacto" style="display:inline-block;background:#221c2e;color:#faf8f4;text-decoration:none;padding:12px 22px;font-weight:600">Agendar una consulta</a></p>
            <div style="border-top:1px solid #e5e2ea;margin-top:26px;padding-top:16px;color:#555;font-size:13px;line-height:1.6">
              <p style="margin:0;font-weight:700;color:#2d1b4e">GEN+ Igualdad</p>
              <p style="margin:0;color:#888">Consultora en género, diversidad e inclusión · Argentina y España</p>
              <p style="margin:8px 0 0">Web: <a href="https://www.genigualdad.com" style="color:#178f89;text-decoration:none">genigualdad.com</a> &nbsp;·&nbsp; Email: <a href="mailto:contacto@genigualdad.com" style="color:#178f89;text-decoration:none">contacto@genigualdad.com</a></p>
              <p style="margin:2px 0 0">Tel: +54 911 6229-6664 (Argentina) &nbsp;·&nbsp; +34 698 187 971 (España)</p>
            </div>
          </div>
        `,
      });
    } catch (e) {
      // No bloqueamos la respuesta si la copia al lead falla: el aviso al equipo ya se envió.
    }
  }

  return res.status(200).json({ message: "Mensaje recibido correctamente" });
}

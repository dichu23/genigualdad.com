import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { nombre, email, telefono, pais, mensaje, empresa_web } = req.body || {};

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

  return res.status(200).json({ message: "Mensaje recibido correctamente" });
}

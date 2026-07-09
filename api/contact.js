// Endpoint de contacto y copia de informe al lead (Resend)
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

// ---- Helpers de formato (sin depender de Intl/ICU) ----
const fmtN = (v) =>
  (Math.round(Number(v) || 0)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
const fmtPct = (v) => {
  const r = Math.round((Number(v) || 0) * 10) / 10;
  return r.toString().replace(".", ",") + "%";
};
const esc = (s) =>
  String(s == null ? "" : s).replace(/</g, "&lt;").replace(/>/g, "&gt;");

// Paleta
const TEAL = "#4aa9a4";
const PURPLE = "#3d2a6e";

// Barra horizontal (comparador nacional): etiqueta · barra · valor
function benchBar(label, val, color, scale) {
  const w = Math.max(2, Math.round((val / scale) * 100));
  return `
    <tr>
      <td style="font:14px Arial,sans-serif;color:#221c2e;padding:5px 10px 5px 0;white-space:nowrap">${label}</td>
      <td style="padding:5px 0;width:100%">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#f4f0e8" style="border-collapse:collapse;background:#f4f0e8">
          <tr>
            <td width="${w}%" bgcolor="${color}" style="background:${color};height:20px;line-height:20px;font-size:1px">&nbsp;</td>
            <td style="font-size:1px;line-height:20px">&nbsp;</td>
          </tr>
        </table>
      </td>
      <td style="font:700 14px Arial,sans-serif;color:#221c2e;padding:5px 0 5px 10px;text-align:right;white-space:nowrap">${fmtPct(val)}</td>
    </tr>`;
}

// Barra de salario por categoría
function salBar(label, val, color, maxSal, cur) {
  const w = Math.max(3, Math.round((val / maxSal) * 100));
  return `
    <tr>
      <td style="font:13px Arial,sans-serif;color:#6b6178;padding:3px 10px 3px 0;white-space:nowrap;width:70px">${label}</td>
      <td style="padding:3px 0;width:100%">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#f4f0e8" style="border-collapse:collapse;background:#f4f0e8">
          <tr>
            <td width="${w}%" bgcolor="${color}" style="background:${color};height:16px;line-height:16px;font-size:1px">&nbsp;</td>
            <td style="font-size:1px;line-height:16px">&nbsp;</td>
          </tr>
        </table>
      </td>
      <td style="font:13px Arial,sans-serif;color:#221c2e;padding:3px 0 3px 10px;text-align:right;white-space:nowrap">${cur} ${fmtN(val)}</td>
    </tr>`;
}

// Informe HTML rico para el lead, con gráficos en tablas (compatibles con email)
function buildLeadReportHtml(nombre, d) {
  const cur = d.cur || "€";
  const gap = Number(d.gap) || 0;
  const absG = Math.abs(gap);
  const gLabel = d.weighted ? "Brecha de género ponderada" : "Brecha de género media";

  let bandBg, bandFg, bandLabel, bandMsg;
  if (absG < 5) {
    bandBg = "#e3f4ee"; bandFg = "#1f6b52"; bandLabel = "Brecha de género baja";
    bandMsg = "La diferencia es pequeña. Conviene documentarla igual en el registro retributivo y revisar que no se concentre en alguna categoría.";
  } else if (absG < 25) {
    bandBg = "#fdf0dc"; bandFg = "#8a5a12"; bandLabel = "Brecha de género media";
    bandMsg = "Hay una diferencia relevante. Revisá si responde a la estructura de puestos o a diferencias en igual trabajo, y dejá registrada la explicación.";
  } else {
    bandBg = "#f6e0e6"; bandFg = "#8a1f3d"; bandLabel = "Brecha de género alta";
    bandMsg = "La diferencia iguala o supera el 25%. En España, en empresas de 50+ personas, este nivel obliga a justificar por escrito que no responde al sexo. Recomendamos una auditoría retributiva.";
  }
  if (gap < 0) {
    bandMsg = "En promedio, las mujeres cobran más que los hombres en los datos cargados. Verificá que los salarios estén cargados en la columna correcta.";
    if (gap < -5) bandLabel = "Revisá la carga";
  }

  // Comparador nacional
  const natGap = Number(d.natGap) || 0;
  let benchHtml = "";
  if (gap > 0 && natGap > 0) {
    const scale = Math.max(gap, natGap) * 1.15;
    const diff = gap - natGap;
    const cmp = Math.abs(diff) < 0.5 ? "en línea con" : diff < 0 ? "por debajo de" : "por encima de";
    benchHtml = `
      <p style="font:600 12px Arial,sans-serif;letter-spacing:.6px;text-transform:uppercase;color:#40365a;margin:26px 0 8px">Tu brecha de género vs. la media de ${esc(d.pais)}</p>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse">
        ${benchBar("Tu organización", gap, TEAL, scale)}
        ${benchBar("Media " + esc(d.pais), natGap, "#b9b2c6", scale)}
      </table>
      <p style="font:13px Arial,sans-serif;color:#6b6178;margin:8px 0 0">Tu brecha de género está <strong>${cmp}</strong> la media nacional (${fmtPct(natGap)}). Fuente: ${esc(d.natSrc || "")}.</p>`;
  }

  // Gráfico por categoría
  const rows = Array.isArray(d.rows) ? d.rows : [];
  let maxSal = 0;
  rows.forEach((c) => { maxSal = Math.max(maxSal, Number(c.w) || 0, Number(c.m) || 0); });
  let chartHtml = "";
  if (rows.length && maxSal > 0) {
    let _sw=0,_sm=0,_nw=0,_nm=0;
    rows.forEach((c)=>{ if(Number(c.nw)>0){_sw+=Number(c.nw)*Number(c.w);_nw+=Number(c.nw);} if(Number(c.nm)>0){_sm+=Number(c.nm)*Number(c.m);_nm+=Number(c.nm);} });
    const _wgt=_nw>0&&_nm>0;
    const _avgW=_wgt?_sw/_nw:(rows.reduce((a,c)=>a+(Number(c.w)||0),0)/rows.length);
    const _avgM=_wgt?_sm/_nm:(rows.reduce((a,c)=>a+(Number(c.m)||0),0)/rows.length);
    const _md=_avgM-_avgW;
    const moneyLine = _md>0 ? `<p style="font:14px Arial,sans-serif;color:#221c2e;margin:16px 0 0">En promedio, los hombres ganan <strong>${cur} ${fmtN(_md)}</strong> más que las mujeres.</p>` : (_md<0 ? `<p style="font:14px Arial,sans-serif;color:#221c2e;margin:16px 0 0">En promedio, las mujeres ganan <strong>${cur} ${fmtN(-_md)}</strong> más que los hombres.</p>` : "");
    chartHtml = `
      <p style="font:600 12px Arial,sans-serif;letter-spacing:.6px;text-transform:uppercase;color:#40365a;margin:26px 0 6px">Salario medio por categoría (mujeres vs. hombres)</p>
      <p style="font:12px Arial,sans-serif;color:#6b6178;margin:0 0 8px">
        <span style="display:inline-block;width:11px;height:11px;background:${TEAL}">&nbsp;</span> Mujeres &nbsp;&nbsp;
        <span style="display:inline-block;width:11px;height:11px;background:${PURPLE}">&nbsp;</span> Hombres
      </p>
      ${rows.map((c) => `
        <div style="margin:14px 0">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font:700 14px Arial,sans-serif;color:#221c2e">${esc(c.name)}</td>
            <td style="font:700 13px Arial,sans-serif;color:${TEAL};text-align:right">brecha de género ${fmtPct(c.gap)}</td>
          </tr></table>
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;margin-top:4px">
            ${salBar("Mujeres", Number(c.w) || 0, TEAL, maxSal, cur)}
            ${salBar("Hombres", Number(c.m) || 0, PURPLE, maxSal, cur)}
          </table>
        </div>`).join("")}${moneyLine}`;
  }

  const repTxt = d.rep != null ? fmtPct(d.rep) : "—";
  const repSub = d.plantilla ? `${fmtN(d.totMuj)} de ${fmtN(d.plantilla)} personas` : "";
  const org = d.org ? esc(d.org) : "";

  return `
  <div style="background:#f1eee8;padding:24px 0;font-family:Arial,sans-serif">
    <table role="presentation" width="600" align="center" cellpadding="0" cellspacing="0" style="width:600px;max-width:100%;margin:0 auto;background:#ffffff;border:1px solid #e5e2ea">
      <tr><td style="padding:28px 32px 8px;text-align:center">
        <img src="https://www.genigualdad.com/img/logo-principal.png" alt="GEN+ Igualdad" width="150" style="width:150px;max-width:60%;height:auto">
      </td></tr>
      <tr><td style="padding:8px 32px 0">
        <p style="font:600 12px Arial,sans-serif;letter-spacing:.8px;text-transform:uppercase;color:#4aa9a4;margin:0">Informe de brecha salarial de género</p>
        <h1 style="font:600 22px Georgia,serif;color:#221c2e;margin:6px 0 2px">Hola ${esc(nombre)}, acá está tu informe</h1>
        <p style="font:14px Arial,sans-serif;color:#6b6178;line-height:1.5;margin:6px 0 0">${org ? "Organización: <strong>" + org + "</strong> · " : ""}País: ${esc(d.pais)}</p>
      </td></tr>

      <tr><td style="padding:18px 32px 0">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:separate;border-spacing:8px 0">
          <tr>
            <td width="33%" style="background:#faf8f4;padding:14px 12px;vertical-align:top">
              <div style="font:600 10px Arial,sans-serif;letter-spacing:.4px;text-transform:uppercase;color:#40365a">${gLabel}</div>
              <div style="font:600 26px Georgia,serif;color:#221c2e;margin-top:4px">${fmtPct(gap)}</div>
            </td>
            <td width="33%" style="background:#faf8f4;padding:14px 12px;vertical-align:top">
              <div style="font:600 10px Arial,sans-serif;letter-spacing:.4px;text-transform:uppercase;color:#40365a">Representación fem.</div>
              <div style="font:600 26px Georgia,serif;color:#221c2e;margin-top:4px">${repTxt}</div>
              <div style="font:11px Arial,sans-serif;color:#6b6178;margin-top:2px">${repSub}</div>
            </td>
            <td width="33%" style="background:#faf8f4;padding:14px 12px;vertical-align:top">
              <div style="font:600 10px Arial,sans-serif;letter-spacing:.4px;text-transform:uppercase;color:#40365a">Plantilla</div>
              <div style="font:600 26px Georgia,serif;color:#221c2e;margin-top:4px">${fmtN(d.plantilla)}</div>
              <div style="font:11px Arial,sans-serif;color:#6b6178;margin-top:2px">${d.cats} categoría${d.cats > 1 ? "s" : ""}</div>
            </td>
          </tr>
        </table>
      </td></tr>

      <tr><td style="padding:16px 32px 0">
        <span style="display:inline-block;background:${bandBg};color:${bandFg};font:700 11px Arial,sans-serif;letter-spacing:.4px;text-transform:uppercase;padding:6px 12px">${bandLabel}</span>
        <p style="font:14px Arial,sans-serif;color:#3a3348;line-height:1.55;margin:12px 0 0"><strong>${fmtPct(gap)}</strong> — ${bandMsg}</p>
        ${benchHtml}
        ${chartHtml}
      </td></tr>

      <tr><td style="padding:22px 32px 0">
        <p style="font:14px Arial,sans-serif;color:#3a3348;line-height:1.55;margin:0">Si la brecha de género te dio media o alta, en Gen+ Igualdad hacemos la <strong>auditoría retributiva</strong> completa: diagnóstico, valoración de puestos y plan de actuación. La primera consulta es sin costo.</p>
        <p style="margin:16px 0 0"><a href="https://www.genigualdad.com/contacto" style="display:inline-block;background:#221c2e;color:#faf8f4;text-decoration:none;padding:13px 26px;font:700 13px Arial,sans-serif;letter-spacing:.4px">Agendar una consulta</a></p>
      </td></tr>

      <tr><td style="padding:24px 32px 28px">
        <div style="border-top:1px solid #e5e2ea;padding-top:18px">
          <img src="https://www.genigualdad.com/img/logo-secundario.png" alt="GEN+ Igualdad" width="120" style="width:120px;height:auto;margin-bottom:8px">
          <p style="font:13px Arial,sans-serif;color:#888;line-height:1.6;margin:0">Consultora en género, diversidad e inclusión · Argentina y España</p>
          <p style="font:13px Arial,sans-serif;color:#555;line-height:1.6;margin:6px 0 0">Web: <a href="https://www.genigualdad.com" style="color:#178f89;text-decoration:none">genigualdad.com</a> &nbsp;·&nbsp; Email: <a href="mailto:contacto@genigualdad.com" style="color:#178f89;text-decoration:none">contacto@genigualdad.com</a></p>
          <p style="font:13px Arial,sans-serif;color:#555;line-height:1.6;margin:2px 0 0">Tel: +54 911 6229-6664 (Argentina) &nbsp;·&nbsp; +34 698 187 971 (España)</p>
        </div>
      </td></tr>
    </table>
  </div>`;
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { nombre, email, telefono, pais, mensaje, empresa_web, copiaAlLead, datos } =
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
  let copyOk = null;
  let copyErr = null;
  if (copiaAlLead) {
    // Espaciamos el segundo envío para respetar el límite de 2 req/seg de Resend.
    await new Promise((r) => setTimeout(r, 700));

    const leadHtml =
      datos && typeof datos === "object"
        ? buildLeadReportHtml(clean(nombre), datos)
        : `
          <div style="font-family:Arial,sans-serif;color:#221c2e;max-width:560px">
            <img src="https://www.genigualdad.com/img/logo-horizontal.png" alt="GEN+ Igualdad" width="220" style="width:220px;max-width:60%;height:auto;margin-bottom:18px">
            <h2 style="color:#2d1b4e">Hola ${clean(nombre)}, acá está tu informe</h2>
            <div style="background:#f8f5ff;border-left:4px solid #5bc4bf;padding:16px;white-space:pre-wrap;font-size:15px">${clean(mensaje)}</div>
            <p style="margin-top:20px"><a href="https://www.genigualdad.com/contacto" style="display:inline-block;background:#221c2e;color:#faf8f4;text-decoration:none;padding:12px 22px;font-weight:600">Agendar una consulta</a></p>
          </div>`;

    try {
      const { error: e2 } = await resend.emails.send({
        from: "Gen+ Igualdad <contacto@genigualdad.com>",
        to: [email],
        replyTo: "contacto@genigualdad.com",
        reply_to: "contacto@genigualdad.com",
        subject: "Tu informe de brecha salarial de género · Gen+ Igualdad",
        html: leadHtml,
      });
      if (e2) {
        copyOk = false;
        copyErr = e2.message || JSON.stringify(e2);
        console.error("Copia al lead falló (Resend):", e2);
      } else {
        copyOk = true;
      }
    } catch (e) {
      copyOk = false;
      copyErr = e && e.message ? e.message : String(e);
      console.error("Copia al lead lanzó excepción:", e);
    }
  }

  return res
    .status(200)
    .json({ message: "Mensaje recibido correctamente", copyOk, copyErr });
}

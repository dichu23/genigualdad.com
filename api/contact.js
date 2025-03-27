// Importar cualquier dependencia necesaria aquí
// Por ejemplo, si quisieras usar nodemailer para enviar emails:
// const nodemailer = require('nodemailer');

import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Method not allowed" });
  }

  const { nombre, email, telefono, mensaje } = req.body;

  const { data, error } = await resend.emails.send({
    from: "Gen Igualdad <contacto@genigualdad.com>",
    to: ["test-a31dpl66j@srv1.mail-tester.com"],
    subject: "Contacto de " + nombre,
    html: `
      <p>Nombre: ${nombre}</p>
      <p>Email: ${email}</p>
      <p>Teléfono: ${telefono}</p>
      <p>Mensaje: ${mensaje}</p>
    `,
  });

  if (error) {
    return res.status(500).json({
      message: "Error al enviar el mensaje",
      error: error.message,
    });
  }

  return res.status(200).json({
    message: "Mensaje recibido correctamente",
    data: { nombre, email, telefono, mensaje },
  });
}

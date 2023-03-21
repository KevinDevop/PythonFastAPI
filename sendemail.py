import smtplib
import unittest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def codigoEmail(email_corporativo: str, codigo: str):

    from_email = "YourEmail"
    passw = "YourPassword"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = email_corporativo
    msg['Subject'] = "Codigo verificación"

    html = """\
    <html lang="es">
      <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
          body {{
            font-family: Arial, sans-serif;
          }}
          h1 {{
            color: #2c3e50;
            font-size: 24px;
            margin-bottom: 20px;
          }}
          p {{
            color: #34495e;
            font-size: 16px;
            margin-bottom: 10px;
          }}
          .code {{
            color: #e74c3c;
            font-size: 20px;
            font-weight: bold;
          }}
        </style>
      </head>
      <body>
        <h1>Código de verificación</h1>
        <span class="code">{}</span>
      </body>
    </html>
    """.format(codigo)

    html = MIMEText(html, 'html')

    msg.attach(html)

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(from_email, passw)
            smtp.sendmail(from_email, email_corporativo, msg.as_string())
            print("Correo enviado exitosamente")
    except Exception as e:
        print("Error al enviar Correo: ", e)


class testemails(unittest.TestCase):

    def test_enviar_correo(self):
        email_corpo = "kemoasmer5665@gmail.com"
        codigo = "12345"
        self.assertEqual(codigoEmail(email_corpo, codigo))


if __name__ == "__main__":
  unittest.main()
# Importamos las librerías necesarias
from email.message import EmailMessage
import ssl
import smtplib
import imghdr


# Creamos las variables para utilizar en el envío del email
email_emisor = 'codehu3@gmail.com'
email_password = 'kcdcwxsrvnbmmpbq'
email_receptor = 'antuboccalandro5@gmail.com'

# Generamos todo el email
# Asunto
subject = 'Python te ha enviado un correo'

# Cuerpo del email
body = '''
Este es un correo electrónico creado con Python
'''

# Creamos el objeto email
em = EmailMessage()

# Configuramos el objeto con los datos del emisor y receptor del correo
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = subject


# Adjuntar archivo al email
with open('python.png', 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name
    em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')


# Generamos un certificado SSL. Este se puede instalar desde donde está instalado Python, pero si no creamos un certificado SSL sin verficiar para evitar errores
context = ssl._create_unverified_context()

# Enviamos el email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Nos logeamos en gmail.com
    smtp.login(email_emisor, email_password)
    # Enviamos el email
    smtp.sendmail(email_emisor, email_receptor, em.as_string())

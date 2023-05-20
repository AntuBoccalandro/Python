import yagmail

email_sender = 'codehu3@gmail.com'
password_sender = 'pywnojlnbihwygpk'

yag = yagmail.SMTP(user=email_sender, password=password_sender)

addressees = ['antuboccalandro5@gmail.com', 'giordanocarla0@gmail.com', 'chamu498@gmail.com']
subject = 'Este es un correo enviado con Python'
message = 'Mensage de prueba enviado con Python'
html='<h1>Mensage de prueba enviado con Python</h1>'
attachment = '/content/python.png'

yag.send(addressees, subject, [message, html], attachments=[attachment])

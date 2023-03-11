import pandas as pd
import smtplib
import ssl

# Credenciales del que envía los correos
name_account = 'Code Hub'
email_account = 'codehu3@gmail.com'
password_account = 'irhjeahkonegdqwb'

# Autenticación y login
# Según usemos gmail, outlook cambiarán los dos parámetros de email y puerto
# Autenticación y login
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_account, password_account)

# Leemos el excel para enviar todos los correos
email_df = pd.read_excel("/content/Emails.xlsx")

# Obtenemos los valores de cada columna
all_names = email_df['Name']
all_emails = email_df['Email']
all_subjects = email_df['Subject']
all_messages = email_df['Message']

for i in range(len(email_df)):

    name = all_names[i]
    email = all_emails[i]
    
    # Personalized subject
    subject = all_subjects[i] + ', ' + all_names[i] + '!'
    
    # Personalized message
    message = ('Hey, ' + all_names[i] + '!\n\n' +
              all_messages[i] + '\n\n'
              'Te deseamos lo mejor,\n' +
              name_account)

    # Generate email to be sent
    sent_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(name_account, email_account, name, email, subject, message))
    
    # Send emails, the reason will be displayed in case you get an error
    try:
        server.sendmail(email_account, [email], sent_email) # [email] is a list that can contain multiple emails
    except Exception:
        print('Could not send email to {}. Error: {}\n'.format(email, str(Exception)))

# Close smtp server
server.close()

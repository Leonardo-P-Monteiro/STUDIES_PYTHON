import os
import dotenv
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

dotenv.load_dotenv()

# CAMINHO ARQUIVO
ARQUIVO_ENVIAR = pathlib.Path(__file__).parent / 'temp_text.txt'

# DADOS REMETENTE
remetente = os.getenv('FROM_EMAIL','')
destinatario = 'poteraskaban@gmail.com'

# CONFIGURAÇÕES
SMTP_SERVER = os.getenv('SMTP_SERVER', '')
SMTP_PORT = 587
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')

# CARREGANDO INFORMAÇÕES DO ARQUIVO PARA ENVIAR NO CORPO DO EMAIL.
with open(ARQUIVO_ENVIAR, 'r', encoding='UTF8') as arquivo:
    texto_arquivo = arquivo.read()
    arquivo.close()

# TRANFORMANDO A MENSAGEM EM MIMIMULTIPART
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Email Teste'

corpo_email = MIMEText(texto_arquivo, 'plain')
mime_multipart.attach(corpo_email)

# ENVIAR O E-MAIL
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.ehlo()
server.starttls()
server.login(SMTP_USERNAME, SMTP_PASSWORD)
server.send_message(mime_multipart)
server.quit()




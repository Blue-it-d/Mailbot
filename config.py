import getpass
import os
import tomli

with open('config.toml') as file:
    content = file.read()
    content_dict = tomli.loads(content)
imapserver = content_dict['imapserver']
bot_address = content_dict['bot_address']
TRUSTED_SENDERS = content_dict['trusted_senders']
pwd = content_dict['password']
smtp_server = content_dict['smtpserver']

if not pwd:
    pwd = getpass.getpass("Account password:")
#bot_address = input ("Address to log in to: ")
#imapserver = input ("IMAP server domain:")
#imapserver = os.getenv('SERVER_NAME')
#bot_address = os.getenv('BOT_ADDRESS')
#trusted_addresses = os.getenv("TRUSTED_SENDERS")
#imapserver = "imap-mail.outlook.com"
#bot_address = "blueit@outlook.de"
#print(imapserver, bot_address)
##smtpserver = input ("SMTP server domain:")
##smtpserverport = input ("SMTP server port [587]:")
# if not smtpserverport or smtpserverport == "":
#    smtpserverport = 587

#pwd = getpass.getpass("Account password:")


#check_freq = 5


commands = {"hello": "xx"}

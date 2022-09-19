import getpass
import os
#bot_address = input ("Address to log in to: ")
#imapserver = input ("IMAP server domain:")
#imapserver = os.getenv('SERVER_NAME')
#bot_address = os.getenv('BOT_ADDRESS')
#trusted_addresses = os.getenv("TRUSTED_SENDERS")
imapserver = "imap-mail.outlook.com"
bot_address = "blueit@outlook.de"
print(imapserver, bot_address)
##smtpserver = input ("SMTP server domain:")
##smtpserverport = input ("SMTP server port [587]:")
# if not smtpserverport or smtpserverport == "":
#    smtpserverport = 587

pwd = getpass.getpass("Account password:")


check_freq = 5


commands = {"hello": "xx"}

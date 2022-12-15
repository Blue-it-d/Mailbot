"""Module providing classes to deal with Mails."""

import email
import smtplib
import imapclient
import pyzmail
from config import *

# IAMP Object
class IAMP:
    def __init__(self):
        self.imapObj = imapclient.IMAPClient(imapserver)
        self.imapObj.login(bot_address, pwd)
        self.imapObj.select_folder("INBOX", readonly=True)
        #print('%d messages in INBOX' % select_info[b'EXISTS'])
    
    @staticmethod
    def build_search_query():
        '''
         Retrun only unseen Emails and from trusted Email-Addresses.
        '''
        searchQuery = []
        if (len(TRUSTED_SENDERS) == 1):
            searchQuery.append(["FROM", TRUSTED_SENDERS[0]])
        if (len(TRUSTED_SENDERS) == 2):
            searchQuery.append("OR")
            searchQuery.append(["FROM", TRUSTED_SENDERS[0]])
            searchQuery.append(["FROM", TRUSTED_SENDERS[1]])
        if (len(TRUSTED_SENDERS) > 2):
            searchQuery.append("OR")
            searchQuery.append(["FROM", TRUSTED_SENDERS[0]])
            searchQuery.append(["FROM", TRUSTED_SENDERS[1]])
            for m in range(2, len(TRUSTED_SENDERS)):
                searchQuery.insert(0, ["FROM", TRUSTED_SENDERS[m]])
                searchQuery.insert(0, "OR")
        searchQuery.insert(0, "UNSEEN")
        print("searchQuery", searchQuery)
        return searchQuery

    def get_unread(self):
        """
        Get unreaded mails
        returns the mails as raw data or None if nothings found
        """
        uids = self.imapObj.search(self.build_search_query())
        if not uids:
            return None
        else:
            print("Found %s unreads" % len(uids))
            return self.imapObj.fetch(uids, ['BODY[]', 'FLAGS'])
    
    @staticmethod
    def get_content(mails, key):
        """
        Analyze the content of the email
        It retruns the content of the email or None if the Email is empty
        """
        msg = pyzmail.PyzMessage.factory(mails[key][b'BODY[]'])
        # Check if message is empty
        if msg.text_part is None:
            print("No text part, cannot parse")
            return None
        text = msg.text_part.get_payload().decode(msg.text_part.charset)
        return text


# SMTP Object
class SMTP:
    def __init__(self):
        print(SMTP_SERVER, pwd, bot_address)
        self.smtpObj = smtplib.SMTP(SMTP_SERVER, 587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.login(bot_address, pwd)


    def send_email(self, to, subject, content, file):
        """
        Send an email to the given address with the given subject and content 
        and attach the given file if it exists otherwise it will be ignored.
        """
        msg = email.message.EmailMessage()
        msg['Subject'] = subject
        msg['From'] = bot_address
        msg['To'] = to
        msg.set_content(content)
        if file is not None:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                    file_name = f.name
            except FileNotFoundError:
                file_data = None
                file_name = None
            if file_data is not None:
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        self.smtpObj.send_message(msg)
        print("Email sent to %s" % to)

    def quit(self):
        """
        Quit the SMTP connection
        """
        self.smtpObj.quit()


# For tests

""" smtp_obj = SMTP()
# send email to example.come with the content: "Hello World"
smtp_obj.send_email("example.com", "Hello World", "Hello World")
smtp_obj.quit()

iamp = IAMP()
#iamp.imapObj.idle()
imapobj = IAMP()
unread = imapobj.get_unread()
if unread:
    content = imapobj.analyze_content(unread, list(unread.keys())[0])
    print("content", content)
else:
    print("no Mails")
 """
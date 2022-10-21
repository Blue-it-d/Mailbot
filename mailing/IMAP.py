from config import *
import imapclient
import email
import pyzmail

# IAMP Object
class IAMP:
    def __init__(self):
        self.imapObj = imapclient.IMAPClient(imapserver)
        self.imapObj.login(bot_address, pwd)
        self.imapObj.select_folder("INBOX", readonly=True)
        #print('%d messages in INBOX' % select_info[b'EXISTS'])

    def build_search_query(self):
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

    def analyze_content(self, mails, key):
        """
        Analyze the content of the email
        It retruns the content of the email or None if the Email is empty
        """
        msg = pyzmail.PyzMessage.factory(mails[key][b'BODY[]'])
        # Check if message is empty
        if msg.text_part is None:
            print("Email is empty")
            return None
        text = msg.text_part.get_payload().decode(msg.text_part.charset)
        return text



iamp = IAMP()
#iamp.imapObj.idle()
imapobj = IAMP()
unread = imapobj.get_unread()
if unread:
    content = imapobj.analyze_content(unread, list(unread.keys())[0])
    print("content", content)
else:
    print("no Mails")

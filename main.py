
from config import *
import imapclient
import pyzmail

def imap_init():
    """
    Initialize IMAP connction
    """
   # print("Initializing IMAP....", end="")
    global i
    i = imapclient.IMAPClient(imapserver)
    c = i.login(bot_address, pwd)
    i.select_folder("INBOX")
    print("DONE. ")


## Get unreaded mails
def get_unread():
    """
    Fetch unread emails
    """
    uids = i.search(['UNSEEN'])
    if not uids:
        return None
    else:
        print("Found %s unreads" % len(uids))
        return i.fetch(uids, ['BODY[]', 'FLAGS'])

def analyze_msg(raws, a):
    print("Analyzing message with uid " + str(a))
    msg = pyzmail.PyzMessage.factory(raws[a][b'BODY[]'])
    sender = msg.get_address("from")
    if sender[1] != trusted_addresses:
        print("Unread is from %s <%s> skipping" % (sender[1],sender[1]))
        return None
    global subject 

    if msg.text_part is None:
        print("No text part, cannot parse")
        return None                                              
    text = msg.text_part.get_payload().decode(msg.text_part.charset)
    cmds = text.replace("\r","").split("\n")
    print(cmds)

imap_init()
msgs = get_unread()

if msgs is not None:
    print("here")
    for msg in msgs.keys():
        print(msg)
        print(type(msg))
        if type(msg) is not int:
            continue
        cmds = analyze_msg(msgs, msg)
else:
    print("No new Mails")



from config import *
import imapclient
import pyzmail

TRUSTED_SENDER = ("test@hotmail.com", "test2@hotmail.com")


def imap_init():
    """
    Initialize IMAP connction
    """
   # print("Initializing IMAP....", end="")
    global i
    i = imapclient.IMAPClient(imapserver)
    c = i.login(bot_address, pwd)
    i.select_folder("INBOX", readonly=True)
    # i.select_folder("INBOX")
    print("DONE. ")


def get_unread():
    """
    Get unreaded mails
    returns the mails as raw data or None if nothings found
    """
    uids = i.search(['UNSEEN'])
    if not uids:
        return None
    else:
        print("Found %s unreads" % len(uids))
        # TODO: Remove readonly=true as these is now true
        # for testing purpose.
        return i.fetch(uids, ['BODY[]', 'FLAGS'])


def isValidSender(sender):
    """
    Check if the given sender is valid
    It compars it with vordefined arrays  
    """
    if sender not in TRUSTED_SENDER:
        print("Unread is from %s skipping" % (sender))
        return False
    return True


def analyze_msg(raws, a):
    print("Analyzing message with uid " + str(a))
    msg = pyzmail.PyzMessage.factory(raws[a][b'BODY[]'])
    sender = msg.get_address("from")
    # Check if a valid sender
    if not isValidSender(sender[1]):
        return None
    global subject
    if msg.text_part is None:
        print("No text part, cannot parse")
        return None
    text = msg.text_part.get_payload().decode(msg.text_part.charset)
    cmds = text.replace("\r", "").split("\n")


imap_init()
msgs = get_unread()

if msgs is not None:
    for msg in msgs.keys():
        print(type(msg))
        if type(msg) is not int:
            continue
        cmds = analyze_msg(msgs, msg)
else:
    print("No new Mails")

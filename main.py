from config import *
import imapclient
import pyzmail
import time

TRUSTED_SENDERS = ("test@hotmail.com", "test2@hotmail.com",)


def imap_init():
    """
    Initialize IMAP connction
    """
   # print("Initializing IMAP....", end="")
    global i
    i = imapclient.IMAPClient(imapserver)
    c = i.login(bot_address, pwd)
    select_info = i.select_folder("INBOX", readonly=True)
    print('%d messages in INBOX' % select_info[b'EXISTS'])
    # i.select_folder("INBOX")
    print("DONE. ")


def build_search_query():
    '''
     Retrun only unseen Emails and from trusted Email-Addresses.
    '''
    searchQuery = []
    if (len(TRUSTED_SENDERS) == 1):
        searchQuery.append("FROM" + TRUSTED_SENDERS[0])
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
    print("search", searchQuery)
    return searchQuery


def get_unread():
    """
    Get unreaded mails
    returns the mails as raw data or None if nothings found
    """
    uids = i.search(build_search_query())
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
    if sender not in TRUSTED_SENDERS:
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
    if cmds[1] not in commands:
        print("not in commands")
        return False
    else:
        return cmds


imap_init()
emails = get_unread()

""" while True:
    try:
        emails = get_unread()
        while emails is None:
            time.sleep(check_freq)
            emails = get_unread()
        for email in emails.keys():
            if type(email) is not int:
                continue
            cmds = analyze_msg(emails, email)
            if cmds is None:
                continue
            elif cmds is False:
                print("command is invalid")
            else:
                print("command recieved: \n %s" % cmds)
    except KeyboardInterrupt:
        i.logout() """

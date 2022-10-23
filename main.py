from config import *
import controlweb

def isValidSender(sender):
    """
    Check if the given sender is valid
    It compars it with vordefined arrays
    """
    if sender not in TRUSTED_SENDERS:
        print("Unread is from %s skipping" % (sender))
        return False
    return True


""" from controlweb.controlweb import control_web
obj = control_web()
obj.navigiate_to("https://python.org")
 """
from mailing.config import *
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



# import IAMP class
from mailing.mailing import IAMP
from controlweb.jobs import commands, add_user_data, add_contract_data, add_department_data

iamp_obj = IAMP()
mails = iamp_obj.get_unread()

if mails is not None:
    for key in mails.keys():
        content = iamp_obj.get_content(mails, key)
        if content is not None:
            cmds = content.replace("\r", "").split("\n")
            cmd = cmds[1]
            #TODO analyse content more prpoerly
            #TODO check if all required data is there after specifying the commands
            if cmd in commands:
                commands[cmd]()
        else:
            print("No content")

""" from controlweb.controlweb import control_web
obj = control_web()
obj.navigiate_to("https://python.org")
 """
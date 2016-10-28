import os
from mailbox import mbox

__location__ = os.path.dirname(os.path.realpath(__file__))
mboxDir = os.path.join(__location__, "Takeout", "Mail")

for file in os.listdir(mboxDir):
	mboxPath = os.path.join(mboxDir, file)
	mboxObj = mbox(mboxPath)
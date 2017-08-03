# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename: request.py

import itchat
from tuling import getResponse

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return getResponse(msg["Text"])["text"]




itchat.auto_login(enableCmdQR=2)
itchat.run()
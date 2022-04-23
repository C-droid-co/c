__mod_name__ = "Greetings"
__help__ = """
/captcha [ENABLE|DISABLE] - Enable/Disable captcha.
/set_welcome - Reply this to a message containing correct
format for a welcome message, check end of this message.
/del_welcome - Delete the welcome message.
/get_welcome - Get the welcome message.
**SET_WELCOME ->**
The format should be something like below.
```
**Hi** {name} Welcome to {chat}
~ #This separater (~) should be there between text and buttons, remove this comment also
button=[Duck, https://duckduckgo.com]
button2=[Github, https://github.com]
```
**NOTES ->**
for /rules, you can do /filter rules to a message
containing rules of your groups whenever a user
sends /rules, he'll get the message
Checkout /markdownhelp to know more about formattings and other syntax.
"""

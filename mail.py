import utils
import msg_test
import msg_managers
import applescript

ASCRIPT = """\
tell application "Mail"
  activate

  --Create the message
  set theMessage to make new outgoing message with properties {{subject:%(subject)s, content:%(body)s, visible:true}}

  --Set a recipient
  tell theMessage
      %(recipents_commands)s
      %(send)s
  end tell
end tell
"""

def send_msg (module, subject, send=False):
    # Addresses
    cmds = []
    for address in module.TO:
        name, email = address
        cmds.append (applescript.email_to_as (name, email, 'to'))

    for address in module.CC:
        name, email = address
        cmds.append (applescript.email_to_as (name, email, 'cc'))

    # Build message
    send_cmd = ('', 'send')[send]

    ascript = ASCRIPT %({'recipents_commands': '\n'.join(cmds),
                         'body': applescript.asquote(module.BODY),
                         'subject': applescript.asquote(subject),
                         'send': send_cmd})

    # Run it
    applescript.asrun (ascript)

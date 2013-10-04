import subprocess

def asrun(ascript):
  "Run the given AppleScript and return the standard output and error."

  osa = subprocess.Popen(['osascript', '-'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
  return osa.communicate(ascript)[0]

def asquote(astr):
  "Return the AppleScript equivalent of the given string."

  astr = astr.replace('"', '" & quote & "')
  return '"{}"'.format(astr)

def email_to_as (name, email, field):
    return 'make new to recipient at end of %s recipients with properties {name:"%s", address:"%s"}' %(field, name, email)

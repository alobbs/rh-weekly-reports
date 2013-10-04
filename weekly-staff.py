#!/usr/bin/env python

import mail
import utils

def main():
    # Build subject
    date_monday = utils.get_next_friday()
    subject = "Weekly Status Reports (%s)" %(date_monday.strftime('%a, %b %d'))

    # Import the managers message
    import msg_my_staff

    # Send the mail
    mail.send_msg (msg_my_staff, subject, send=False)

if __name__ == '__main__':
    main()

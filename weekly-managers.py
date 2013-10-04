#!/usr/bin/env python

import mail
import utils

def main():
    # Build subject
    date_monday = utils.get_next_monday()
    subject = "RHOS Weekly Team Status (%s)" %(date_monday.strftime('%a, %b %d'))

    # Import the managers message
    import msg_managers

    # Send the mail
    mail.send_msg (msg_managers, subject, send=False)

if __name__ == '__main__':
    main()

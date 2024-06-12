from entity.emails.gmail import Gmail


def emails():
    gmail = Gmail()
    gmail.get_emails()

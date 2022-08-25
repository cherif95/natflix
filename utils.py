import re


def is_a_valid_email_address(email):
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    else:
        return False

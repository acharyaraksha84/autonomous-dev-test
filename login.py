def login(username, password):

    if not username:
        return False

    if len(password) < 6:
        return False

    return True
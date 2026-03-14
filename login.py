def login(username, password):

    if not password:
        print("Password cannot be empty")
        return False

    print("Login successful")

def validate_username(username):
    if not username:
        return False
    if len(username) < 3:
        return False
    if not username.isalnum():
        return False
    return True

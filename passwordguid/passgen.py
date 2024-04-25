import string
import secrets

# function to generate password based on length
def genPassword(pwlength, mode='standard'):
    # use mode to determine password complexity
    if mode == 'minimum':
        characters = string.ascii_letters
    elif mode == 'advanced':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(int(pwlength)))
    return password

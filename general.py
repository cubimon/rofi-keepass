import pykeepass

def get_kp():
    password = open('.password').read().lstrip().rstrip()
    return pykeepass.PyKeePass('/share/Passwords.kdbx', password=password)


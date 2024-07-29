import getpass

def set_password():
    password = getpass.getpass('Enter your password: ')
    with open('/data/data/com.termux/files/home/.termux_password', 'w') as f:
        f.write(password)
    print("Password set successfully!")

if __name__ == "__main__":
    set_password()

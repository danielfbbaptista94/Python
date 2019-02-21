

while True:
    password = input('Enter a password: ')
    if len(password) >= 5 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        print('Password is ok')
        break
    else:
        print('Password is not ok')

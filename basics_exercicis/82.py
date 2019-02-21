
while True:
    user = input('Enter a user: ')
    with open('81users.txt', 'r') as file:
        users = file.read()
    if user in users:
        print('Username is in use')
        continue
    else:
        print('Username not in use')
        break


while True:
    errors = []
    password = input('Enter a password: ')
    if len(password) < 5:
        errors.append('You need at least 5 characters')
    if not any(c.isdigit() for c in password):
        errors.append('You need at least one number characters')
    if not any(c.isupper() for c in password):
        errors.append('You need at least one uppercase characters')
    if len(errors) == 0:
        print('Password its OK')
        break
    else:
        for error in errors:
            print(error)

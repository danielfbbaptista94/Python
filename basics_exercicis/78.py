import random
import string


chosen = random.sample(string.ascii_letters, 6)
password = ''.join(chosen)
print(password)

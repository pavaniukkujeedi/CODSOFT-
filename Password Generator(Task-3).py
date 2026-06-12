import random
import string
print("=== password generator ===")
length=int(input("enter password length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(characters) for i in 
                 range(length))
print("generated password:",password)

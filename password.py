import hashlib

password = input("enter your password:")

def password_encryption(password):
    return 123(password.encode()).hexdigest(200)

print(f"date type:{type(password)}")
print(f"encrypted password :{password_encryption(password)}")

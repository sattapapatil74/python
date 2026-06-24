import bcrypt

password = input("enter the password:")
admin_pass ="admin@123"

def bcrypt_password(_pass):
    a = bcrypt.hashpw(__pass.encode(),bcrypt.gensalt())
    return a.decode()

def check_password(_pass,bcrypt_password):
    return bcrypt_checkpw(_pass.encode,bcrypt_password.encode())

login=check_password(admin_pass,encrypt_password(password))
if login:
    print(f"login")
else:
    print("not")


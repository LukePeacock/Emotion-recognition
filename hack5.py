import hashlib
#from real_time_video import start_stream

#emos = (start_stream(3,50))


## Encryption function using SHA-2 256 bit hashing
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
    
## Turn emotions array into password by hashing each individually
## then concat them into a string and hash that then return
def create_password(emotions):
    password = ""

    for item in emos:
        password+= encrypt_string(item)
    newpass = encrypt_string(password)
    return newpass

# Test emotion array
emos = ['happy', 'sad', 'happy']
password = create_password(emos)
print(password)

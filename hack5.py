import hashlib
#from real_time_video import start_stream

#emos = (start_stream(3,50))


## Encryption function using SHA-2 256 bit hashing
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
    
## Turn emotions array into password by hashing each individually
## then concat them into a string and hash that then return
def create_password(emotions, emo_num, emo_dur):
    password = ""

    for item in emotions:
        password+= encrypt_string(item)
    password += encrypt_string(emo_num)
    password += encrypt_string(emo_dur)
    newpass = encrypt_string(password)
    return newpass

# Test emotion array
emos = ['happy', 'sad', 'happy']
emo_num = 3
emo_dur = 1
password = create_password(emos, str(emo_num), str(emo_dur))
print(password)

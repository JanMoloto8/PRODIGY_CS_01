
def encrypt_character(character, key, alphabet):
    if character == ' ':
        return '@'
    position = alphabet.index(character)
    
    new_position = (position + key) % len(alphabet)
    return alphabet[new_position]

def encrypt(password, key):
    track_cases=list(password)
    #We shall use this to track the case of the letter in track cases list
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=0
    for c in track_cases:
        if c in alphabet:
            track_cases[i]='Lower'
        elif c in alphabet2:
            track_cases[i]='Upper'
        i+=1
    password = password.lower()
    encrypted_password=''
    for char in password:
        encrypted_password=encrypted_password+str(encrypt_character(char,key,alphabet))

    return encrypted_password.upper(),track_cases #Encrypted password is in uppercase

def decrypt_character(character, key, alphabet):
    if character == '@':
        return ' '  # Keeping spaces intact
    position = alphabet.index(character)
    new_position = (position - key) % len(alphabet)
    return alphabet[new_position]

def decrypt(password, key,cases):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = password.lower()
    decrypted_password = ''.join(decrypt_character(char, key, alphabet) for char in password)
    for i in range(len(cases)):
        if cases[i]=="Upper":
            decrypted_password=decrypted_password[:i]+decrypted_password[i].upper()+decrypted_password[i+1:]
        elif cases[i]=="Lower":
            decrypted_password=decrypted_password[:i]+decrypted_password[i].lower()+decrypted_password[i+1:]
    return decrypted_password

# Input
password = input("Enter your password: ")
key = int(input("Shift key value: "))

# Encrypt and Decrypt
encrypted_password,cases = encrypt(password, key)
decrypted_password = decrypt(encrypted_password, key,cases)

# Output
print("Original password  : ", password)
print("Encrypted password : ", encrypted_password)
print("Decrypted password : ", decrypted_password)

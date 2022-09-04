import cryptocode,os,random
def generate_keystroke():
    ke=[]
    for i1 in range(48):
        ke.append(random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")))
    return "".join(ke)
if not os.path.isfile("keystroke"):
    print("Before the first time using this tool you need to generate a keystroke.")
    print('The keystroke is encrypted and stored in the "keystroke" file.')
    encryptedKeystroke=cryptocode.encrypt(generate_keystroke(),input("Set a password to encrypt the keystroke: "))
    with open("keystroke","w") as file:
        file.write(encryptedKeystroke)
    print("All set! All you need to do now is to send this tool along with the keystroke file to the one who uses this tool together with you.")
encryptedKey=""
with open("keystroke","r") as file:
    encryptedKey=file.read()
key=cryptocode.decrypt(encryptedKey,input("Password: "))
while key==False:
    print("Wrong Password.")
    key=cryptocode.decrypt(encryptedKey,input("Password: "))
while True:
    choice=input("Encrypt or Decrypt? (E/D)")
    while not choice in ["e","E","d","D"]:
        choice=input("Encrypt or Decrypt? (E/D)")
    if choice in ["E","e"]:
        print(cryptocode.encrypt(input("Plaintext: "),key))
    else:
        print(cryptocode.decrypt(input("Ciphertext: "),key))

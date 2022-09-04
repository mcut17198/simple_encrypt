import cryptocode,os,random,pyperclip,getpass
def generate_keystroke():
    ke=[]
    for i1 in range(48):
        ke.append(random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")))
    return "".join(ke)
if not os.path.isfile("keystroke"):
    print("Welcome to Simple Encrypt.")
    print("Before the first time using this tool you need to generate a keystroke.")
    print('The keystroke is encrypted and stored in the "keystroke" file.')
    print()
    encryptedKeystroke=cryptocode.encrypt(generate_keystroke(),getpass.getpass("Set a password to encrypt the keystroke: "))
    with open("keystroke","w") as file:
        file.write(encryptedKeystroke)
    print()
    print("All set!")
    print('If you come across "Pyperclip could not find a copy/paste mechanism for your system." error, install xclip on your system:')
    print()
    print(" $ sudo apt install xclip")
    print()
    print("All you need to do now is to send this tool along with the keystroke file to the one who uses this tool together with you.")
    print()
encryptedKey=""
with open("keystroke","r") as file:
    encryptedKey=file.read()
key=cryptocode.decrypt(encryptedKey,getpass.getpass("Password: "))
while key==False:
    print("Wrong Password.")
    key=cryptocode.decrypt(encryptedKey,getpass.getpass("Password: "))
while True:
    choice=input("Encrypt or Decrypt? (E/D)")
    while not choice in ["e","E","d","D"]:
        choice=input("Encrypt or Decrypt? (E/D)")
    if choice in ["E","e"]:
        content=input("Plaintext(Leave empty to encrypt clipboard): ")
        if content=="":
            content=pyperclip.paste()
        content_encrypted=cryptocode.encrypt(content,key)
        print(content_encrypted)
        pyperclip.copy(content_encrypted)
    else:
        content=input("Ciphertext(Leave empty to decrypt clipboard): ")
        if content=="":
            content=pyperclip.paste()
        content_decrypted=cryptocode.decrypt(content,key)
        print(content_decrypted)
        pyperclip.copy(content_decrypted)
    print()
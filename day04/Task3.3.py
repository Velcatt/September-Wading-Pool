def encrypt(text, key):


def decrypt(text, key):


text = input("Enter a text : ")
key = input("Enter the encryption key : ")
choice = input("type \"a\" to encrypt or \"b\" to decrypt : ")

if(choice=="a"):
    print(encrypt(text,key))
elif(choice=="b"):
    print(decrypt(text,key))
else:
    print("Wrong choice ! Please only type \"a\" or \"b\" in the choice field")

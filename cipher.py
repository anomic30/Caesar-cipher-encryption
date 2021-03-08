#####################################################################################
##  Simple program to demonstrate Caesar cipher encryption technique using Python  ##
##  Author: Anom Chakravorty | Github: anomic30                                    ##
#####################################################################################

import string
def encrypt(text,shift):
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    '''
    encrypted_text=list(range(len(text)))

    alphabet = string.ascii_lowercase
    first_half=alphabet[:shift]
    second_half=alphabet[shift:]
    shifted_alphabet=second_half+first_half
    
    for i,letter in enumerate(text.lower()):
        if letter in alphabet:
            original_index=alphabet.index(letter)
            new_letter=shifted_alphabet[original_index]
            encrypted_text[i]=new_letter
        else:
            encrypted_text[i]=letter
    return ''.join(encrypted_text)

def decrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The original text message.
    '''
    original_text=list(range(len(text)))

    alphabet = string.ascii_lowercase
    first_half=alphabet[:shift]
    second_half=alphabet[shift:]
    shifted_alphabet=second_half+first_half
    
    for i,letter in enumerate(text.lower()):
        if letter in alphabet:
            shifted_index=shifted_alphabet.index(letter)
            new_letter=alphabet[shifted_index]
            original_text[i]=new_letter
        else:
            original_text[i]=letter
    return ''.join(original_text)

def brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message. 
            One of the printed outputs should be readable.
    """
    for n in range(26):
        print("Using a shift value of {}".format(n))
        print("Decrypted text: {}".format(decrypt(message,n)))
        print('\n')

print("<<<< This Python script demonstrates Caesar cipher encryption technique >>>>")
while True:
    print("1. To encrypt text with shift value, press '1'\n2. To decrypt text with shift value, press '2'\n3. For brute force decryption, press '3'")
    print("4. To quit the program, press '4'")
    n=input(">>> ").lower().rstrip()
    if n=='4':
        break
    elif n=='1':
        sent=input("Enter the text to be encrypted: ")
        val=int(input("Enter the shift value: "))
        print("Encryption successfull!")
        print("Encrypted text: {}".format(encrypt(sent,val)))
        print("\n")
    elif n=='2':
        sent=input("Enter the text to be decrypted: ")
        val=int(input("Enter the shift value: "))
        print("Decryption successfull!")
        print("Decrypted text: {}".format(decrypt(sent,val)))
        print("\n")
    elif n=='3':
        sent=input("Enter the text to be decrypted by brute force: ")
        print("Executing brute force method...")
        print(brute_force(sent))
    else:
        print("Invalid choice")

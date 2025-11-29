import sys

#--------------------#
# Encrypt data
#--------------------#

def encrypt(original_text, shift_number, ALPHABET):
    encrypted_data=""
    for letter in original_text:
        new_letter_index=(ALPHABET.index(letter)+shift_number)%len(ALPHABET)
        encrypted_data+=ALPHABET[new_letter_index]
    return encrypted_data

#--------------------#
# Decrypt data
#--------------------#

def decrypt(encrypted_data, shift_number, ALPHABET):
    decrypted_data=""
    for letter in encrypted_data:
        new_letter_index=(ALPHABET.index(letter)-shift_number)%len(ALPHABET)
        decrypted_data+=ALPHABET[new_letter_index]
    return decrypted_data

ALPHABET=[chr(letter) for letter in range(97,123)]
if __name__=="__main__":
    while(True):
        print("1. Encrypt data")
        print("2. Decrypt data")
        print("3. Exit")
        user_choice=int(input("Enter your choice: "))
        if user_choice==1:
            user_input=input("Enter data to Encrypt: ")
            shift_value=int(input("Enter shift number: "))
            encrypted_data=encrypt(user_input, shift_value, ALPHABET)
            print(f"Encrypted data: {encrypted_data}")
        elif user_choice==2:
            user_input=input("Enter your data: ")
            shift_value=int(input("Enter your shift number: "))
            decrypted_data=decrypt(user_input, shift_value, ALPHABET)
            print(f"Decrypted data: {decrypted_data}")
        else:
            sys.exit(1)

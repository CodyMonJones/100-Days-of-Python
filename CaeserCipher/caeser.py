alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(user_message, shift_number):
    encrypted_message = ""
    for letter in user_message:
        original_postion = alphabet.index(letter)
        encrypted_position = original_postion + shift_number
        if encrypted_position > len(alphabet) - 1:
            encrypted_position = encrypted_position - len(alphabet)
        encrypted_message += alphabet[encrypted_position]
    print(encrypted_message)  

def decryption(user_message, shift_number):
    decrypted_message = ""
    for letter in user_message:
        original_position = alphabet.index(letter)
        decrypted_position = original_position - shift_number
        if decrypted_position < 0:
            decrypted_position = decrypted_position + len(alphabet)
        decrypted_message += alphabet[decrypted_position]
    print(decrypted_message)   

def rot13(user_message, shift_number=13):
    rot_message = ""
    for letter in user_message:
        original_position = alphabet.index(letter)
        rot_shift = original_position + 13
        if rot_shift > 26:
            rot_shift = rot_shift - len(alphabet)
        elif rot_shift < 0:
            rot_shift = rot_shift + len(alphabet)             
        rot_message += alphabet[rot_shift]
    print(rot_message)

user_choice = input("Type (e)ncrypt, (d)ecrypt, (r)ot13, (q)uit: ").lower()
while user_choice != 'q':
    if user_choice == 'e':
        user_message = input("Type your message: ").lower()
        shift_number = int(input("How far would you like to shift: "))
        encryption(user_message, shift_number)
    elif user_choice == 'd':
        user_message = input("Type your message: ").lower()
        shift_number = int(input("How far would you like to shift: "))
        decryption(user_message, shift_number)
    elif user_choice == 'r':
        user_message = input("Type your message: ").lower()
        rot13(user_message, shift_number=13)

    user_choice = input("Type (e)ncrypt, (d)ecrypt, (r)ot13, (q)uit: ").lower()    
        
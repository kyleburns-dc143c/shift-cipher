def shift_encrypt(word, shift):
    encrypted = []

    if shift > 25:
        shift %= 25

    for char in word.lower():
        if (ord(char) - shift) < 97:
            new_char = chr(ord(char) - shift + 26)
            encrypted.append(new_char)
        else:
            new_char = chr(ord(char) - shift)
            encrypted.append(new_char)
    return ''.join(encrypted)

def shift_decrypt(encrypted, shift):
    decrypted = []

    if shift > 25:
        shift %= 25

    for char in encrypted:
        if (ord(char) + shift) > 122:
            new_char = chr(ord(char) + shift - 26)
            decrypted.append(new_char)
        else:
            new_char = chr(ord(char) + shift)
            decrypted.append(new_char)
    return ''.join(decrypted)

def main_menu():
    print('''
    [1] Encrypt
    [2] Decrypt
    [3] Exit
    ''')
    user_input = input('Choose what to do: ')

    while True:
        if user_input == '1':
            word = input('Enter the word or phrase to encrypt: ')
            shift = int(input('How many characters to shift by? '))
            print(shift_encrypt(word, shift))
            main_menu()
        elif user_input == '2':
            word = input('Enter the encrypted string: ')
            shift = int(input('How many characters to shift by: '))
            print(shift_decrypt(word, shift))
            main_menu()
        elif user_input == '3':
            exit()
        else:
            main_menu()

if __name__ == '__main__':
    main_menu()
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
]

continue_game = True

def caesar(direction, text, shift):
    result = ""

    if direction == "decode":
        shift *= -1
        
    for char in text:
        if char in alphabet:
            postion = alphabet.index(char)
            new_positon = (postion + shift) % len(alphabet)
            new_letter = alphabet[new_positon]
            result += new_letter
        else:
            result += char

    print(f"The result is:\n{result}")

while continue_game:
    direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction not in ["encode", "decode"]:
        print("Invalid input")
        continue   # restart loop immediately


    text= input("Type your message:\n").lower()
    shift =  int(input("Type the shift number:\n"))

    caesar(direction, text, shift)


    go_again=input("Type 'yes' if you want to go again. Otherwise type 'no'\n") 

    if go_again == 'no':
        continue_game= False
        print("Good bye!")
        break

# the long way below    

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = (position + shift) % len(alphabet)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded code is:\n{cipher_text}")


# def decrypt(text, shift):
#     cipher_text=""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = (position - shift) % len(alphabet)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded code is:\n{cipher_text}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("make sure you give the correct direction: it is either 'encode' or 'decode'")

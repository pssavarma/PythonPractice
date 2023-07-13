aplhabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input_text = input("enter the text that should be encrypted/decrypted: ").lower()
option = input("do you want to encode or decode: ").lower()
shift = int(input("enter the shift value: "))

def encode(plain_text, shift):
    ciphered_text=""
    for i in plain_text:
        place = aplhabet.index(i)
        newplace = place + shift
        ciphered_text = ciphered_text + aplhabet[newplace]
    print(ciphered_text)


def decode(ciphered_text, shift):
    plain_text=""
    for i in ciphered_text:
        place = aplhabet.index(i)
        newplace = place - shift
        plain_text = plain_text + aplhabet[newplace]
    print(plain_text)

if option == 'encode':
    encode(plain_text=input_text, shift=shift)
elif option == 'decode':
    decode(ciphered_text=input_text, shift=shift)
else:
    input_text = input("type enceode or decode to choose one: ")

#need to be improved
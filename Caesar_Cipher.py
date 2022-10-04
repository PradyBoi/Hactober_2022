from logo import art
print(art)
choose= str(input("type 'e' to encrypt and 'd' to decrypt: ")).lower()
if choose == "e":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    txt = str(input("Type your message here\n"))
    shift = int(input("Type shift amount"))
    def encrypt(a,b):
        emp_str = ""
        for letter in a:
            position = alphabet.index(letter)
            new_shift=position+b
            new_letter = alphabet[new_shift]
            emp_str+=new_letter
        print(f"encrypted message = {emp_str}")
    encrypt(a=txt,b=shift)
else:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    e_txt = str(input("Type your message here\n"))
    shifted_amount = int(input("Enter the shift amount: "))
    def decrypt(x,y):
        str = ''
        for l in x:
            position = alphabet.index(l)
            new_position = position-y
            np=alphabet[new_position]
            str+=np
        print(f"decrypted message: {str}")
    decrypt(x=e_txt,y=shifted_amount)

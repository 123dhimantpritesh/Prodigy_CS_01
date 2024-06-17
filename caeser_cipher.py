#caesercipher
#encode-decode
def caesar_cipher(t, s, d):
    result = ""
    for char in t:
        if char.isalpha():
            shift_amount = s % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            if d == "encrypt":
                result += chr((ord(char) - base + shift_amount) % 26 + base)
            elif d == "decrypt":
                result += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            result += char
    return result

# User input
t = input("Enter the text to be encrypted/decrypted : ")
s = int(input("Enter shift value : "))
d = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

# Perform encryption/decryption
if d in ["encrypt", "decrypt"]:
    output = caesar_cipher(t, s, d)
    print(f"The {d}ed text is: {output}")
else:
    print("Invalid direction ! \n  Please choose to 'encrypt' or 'decrypt'.")

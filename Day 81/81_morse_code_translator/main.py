from morse_code import morse_alphabet

def to_morse(text):
    morse = ""
    for char in text:
        if char == "":
            morse += "/"
        elif char in morse_alphabet.keys():
            morse += morse_alphabet[char]
        else:
            morse += char
    return morse

while True:
    text = input("Text to translate?\n").upper()
    result = to_morse(text)
    print(result)
    input("\n\nPress any key to continue...\n\n")
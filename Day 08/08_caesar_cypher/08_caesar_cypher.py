alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0','1', '2', '3', '4', '5','6','7', '8', '9']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. qxuj8lxvx8n01j0

def encrypt(text, shift):
	encrypted = ""
	abc = alphabet + alphabet
	for i in text:
		index_encrypt = abc.index(i) + shift
		encrypted += abc[index_encrypt]
	print(f'ENCODED {text.upper()} = {encrypted}')

def decrypt(text, shift):
	decrypted = ""
	abc = alphabet + alphabet
	for i in text:
		index_decrypt = abc.index(i) + len(alphabet) - shift
		decrypted += abc[index_decrypt]
	print(f'DECODED {text} is: {decrypted}')


if direction == 'encode':
	encrypt(text, shift)
elif direction == 'decode':
	decrypt(text, shift)
else:
	print('Not a valid option')
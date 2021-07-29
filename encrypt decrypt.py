def encrypt():
  message = input("Enter the message you want to encrypt : ")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt : ")
  ascii_message = [ord(char)-3 for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

t=1
while t<2:
	inp=int(input(''' Enter Your Option Number.
1. encrypt, 2. decrypt,3. Exit : '''))
	if inp==1:
		encrypt()
	elif inp==2:
		decrypt()
	elif inp==3:
		print("You Are exit")
		break
	else:
		print("not valid")

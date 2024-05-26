import rsa

#read private key
with open("prv.key", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

#open cipher texts
encrypted_message = open("cipher1.bin", "rb").read()

encrypted_message2 = open("cipher2.bin", "rb").read()

#decrypt cipher text
clear_message = rsa.decrypt(encrypted_message, private_key)

clear_message2 = rsa.decrypt(encrypted_message2, private_key)

print(encrypted_message)
print(encrypted_message2)

#printed messages
print(clear_message)
print(clear_message2)

#added to text documents
with open('AA_plaintxt1.txt', 'w') as f:
    f.write(clear_message.decode('utf-8'))

with open('AA_plaintxt2.txt', 'w') as f:
    f.write(clear_message2.decode('utf-8'))











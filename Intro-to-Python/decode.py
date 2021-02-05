import base64

with open("encodedflag.txt", "r") as f:
		encoded_flag = f.read()

for i in range(5):
	encoded_flag = base64.b16decode(encoded_flag)

for i in range(5):
	encoded_flag = base64.b32decode(encoded_flag)

for i in range(5):
	encoded_flag = base64.b64decode(encoded_flag)

print(encoded_flag)
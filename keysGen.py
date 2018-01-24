from Crypto.PublicKey import RSA
from Crypto import Random
def keygen():
	random_generator = Random.new().read
	key = RSA.generate(1024, random_generator)
	#print key
	public_key = key.publickey()
	data=[key,public_key]
	'''
	enc_data = public_key.encrypt('abcdefgh', 32)
	print enc_data
	print key.decrypt(enc_data)
	signature = key.sign('abcdefgh', '')
	print public_key.verify("abcdefgh", signature)'''
	return data
'''if __name__ == '__main__':
	#name private_key public_key
	a_list = [["shibbu"],["anoop"],["kaju"],["sunchit"],["sur"]]
	for i in range (0,len(a_list)):
		key=keygen()
		a_list[i].extend(key)
	for i in range (0,len(a_list)):
		print(a_list[i][0],a_list[i][1],a_list[i][2])'''


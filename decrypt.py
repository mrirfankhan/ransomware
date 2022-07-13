import os
from cryptography.fernet import Fernet


files1=os.listdir(os.getcwd())
cur=os.getcwd()

with open("scret.key","rb") as file1:
	key1=file1.read()
key2=Fernet(key1)
# print(key2)
for file1 in files1:
	if file1=="scret.key" or file1=="encrypt.py" or file1=="decrypt.py":
		pass

	elif os.path.isdir(file1):
		
		for fi in os.listdir(os.chdir(file1)):
			if os.path.isfile(fi):
				with open(fi,"rb") as f:
					ff=f.read()
				new=key2.decrypt(ff)
				fff=open(fi,"wb")
				fff.write(new)
	else:
		os.chdir(cur)
		with open(file1,"rb") as f:
			ff=f.read()
		new=key2.decrypt(ff)
		with open(file1,"wb") as fff:
			fff.write(new)

    # else:
    #     pass
        # os.chdir(cur)
		# with open(file1,"rb") as f:
		# 	ff=f.read()
		# new=key2.encrypt(ff)
		# with open(file1,"wb") as fff:
		# 	fff.write(new)

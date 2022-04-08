key="";
encrypted_word="";

def K(): 

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from autokey_name import autokey_name;

	from encryption_name import encryption_name;

	from exit_function import exit;

	os.chdir("..");

	os.chdir("Autokey_Cipher/");

	os.chdir("Encryption/");

	a=os.path.abspath("");

	sys.path.append(a);

	from autokey_encryption import inp;

	os.chdir("Key/");
	
	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from autokey_encryption_user_function import User;
	
	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	try:

		global encrypted_word;

		global key;

		key=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");




		clear();




		NAME();


		autokey_name();

		encryption_name();

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		if key=="A":
			
			clear();

			NAME();

			autokey_name();

			encryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_encryption import Encryption;

			Encryption();

		elif key=="B":
			exit();	

		elif key=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_encryption_key import K;

			K();



		k=True;

		if key.isdigit()!=True:
			k=False

		elif int(key)>25:
			k=False

		elif int(key)<0:
			k=False



		if k==False:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+key+'",',"which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_encryption_key import K;

			K();
			



		else:

			print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+key+'"\n'+"\033[0m");

			index=[];
			space=[i for i in range(len(inp)) if inp[i]==" "];
			for i in inp:
				if i==" ":
					pass;
				else:
					index.append(ord(i)-97);
				
			key_list=[int(key)];
			for i in index:
				key_list.append(i);

			encrypt_val=[];
			start=0;
			for en_val in index:
				encrypt_val.append((int(index[start])+key_list[start])%26);
				start=start+1;
			
			encrypt_num=0;
			encrypt_word=[];
			for i in encrypt_val:
				encrypt_num=65+i;
				encrypt_word.append(chr(encrypt_num));
				encrypt_num=0;

			for i in space:
				encrypt_word.insert(i," ");

			encrypted_word="";
			for encrypt_letter in encrypt_word:
				encrypted_word=encrypted_word+encrypt_letter;

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");

			User();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		autokey_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_encryption_key import K;

		K();

	except EOFError:

		clear();


		

		NAME();



		autokey_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_encryption_key import K;

		K();

key2="";
encrypted_word="";

def K2():

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from affine_name import affine_name;

	from encryption_name import encryption_name;

	from exit_function import exit;

	os.chdir("..");

	os.chdir("Affine_Cipher/");

	os.chdir("Encryption/");

	a=os.path.abspath("");

	sys.path.append(a);

	from affine_encryption import inp;

	os.chdir("Key1/");

	a=os.path.abspath("");

	sys.path.append(a);

	from affine_encryption_key1 import key1;

	from affine_encryption_key1 import encrypt_val1;

	os.chdir("Key2/");

	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from affine_encryption_user_function import User;
	
	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	try:

		global encrypted_word;

		global key2;

		key2=input("\033[1;32;40m"+"【A】 Back\n\n【B】 Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key for Additive Encryption in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");

		clear();

		NAME();

		affine_name();

		encryption_name();

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		if key2=="A":
			
			clear();

			NAME();

			affine_name();

			encryption_name();

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_key1 import K1;

			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

			K1();

		elif key2=="B":
			exit();	

		elif key2=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key1/");

			os.chdir("Key2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_key2 import K2;

			K2();

		k=True;

		if key2.isdigit()!=True:
			k=False

		elif int(key2)>25:
			k=False

		elif int(key2)<0:
			k=False



		if k==False:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+key2+'",',"which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key1/");

			os.chdir("Key2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_key2 import K2;

			K2();
		



		else:

			print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");
			
			encrypt_val2=[];
			start=0;
			for en_val in encrypt_val1:
				if en_val==32:
					encrypt_val2.append(32);
					start=start+1;
				else:				
					encrypt_val2.append((int(encrypt_val1[start])+int(key2))%26);
					start=start+1;
			
			encrypt_num=0;
			encrypt_word=[];
			for i in encrypt_val2:
				if i==32:
					encrypt_word.append(chr(32));
				else:				
					encrypt_num=65+i;
					encrypt_word.append(chr(encrypt_num));
					encrypt_num=0;
			
			encrypted_word="";
			for encrypt_letter in encrypt_word:
				encrypted_word=encrypted_word+encrypt_letter;


			
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");

			User();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		affine_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key1/");

		os.chdir("Key2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_key2 import K2;

		K2();

	except EOFError:

		clear();


		

		NAME();



		affine_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key1/");

		os.chdir("Key2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_key2 import K2;

		K2();

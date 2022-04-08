def User():

	import os;

	import sys

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

	os.chdir("Key2/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from affine_encryption_key2 import key2;

	from affine_encryption_key2 import encrypted_word;

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from exit_function import exit;

	from affine_name import affine_name;
	
	from encryption_name import encryption_name;

	try:
		user=input("\033[1;32;40m"+"【1】 Continue\n\n【2】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if user=="1":
		
			clear();

			NAME();

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			from cryptestein import Cryptestein;

			Cryptestein();
	
		elif user=="2":
			exit();
		
		elif user=="":
			clear();
			NAME();
			affine_name();
			encryption_name();
			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 
			print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");
			print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");			
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
			User();

		else:
			clear();
			NAME();
			affine_name();
			encryption_name();			
			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 
			print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");
			print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n"+"\033[0m");			
			User();
																
	except KeyboardInterrupt:

		clear();


		

		NAME();


		affine_name();
		encryption_name();
		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 
		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");
		print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");
		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

	except EOFError:

		clear();


		

		NAME();


		affine_name();
		encryption_name();
		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 
		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");
		print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");
		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

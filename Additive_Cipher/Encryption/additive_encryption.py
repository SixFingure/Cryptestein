inp="";

def Encryption():	

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from clear_function import clear;

	from program_name import NAME;

	from encryption_name import encryption_name;
	
	from help_name import help_name;

	from additive_name import additive_name;

	from exit_function import exit;

	try:



		global inp;
		
		inp=input("\033[1;32;40m"+"【1】 Back\n\n【2】 Exit\n\n"+"\033[1;36;40m"+"Enter the Text you want to Encrypt in Small Alphabets Only : "+"\033[0m");

		clear();

		NAME();

		additive_name();

		encryption_name();

		if inp=="1":

			clear();

			NAME();

			additive_name();
			
			os.chdir("..");

			os.chdir("Additive_Cipher/");

			a=os.path.abspath("");

			sys.path.append(a)

			from additive_cipher import Crypt;
			
			Crypt();

		elif inp=="2":

			exit();

		elif inp=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Additive_Cipher/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_encryption import Encryption;

			Encryption();

		char=False;					
		ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
		for c in inp:

			if c.isdigit() or c.isupper():

				char=True;
				break;
			elif c==chr(92):
					char=True;
					break;
			else:
				for i in ls:
					if i==c:

						char=True;
						break;


		if char==True:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Additive_Cipher/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_encryption import Encryption;

			Encryption();

	

		else:

			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

			os.chdir("..");

			os.chdir("Additive_Cipher/");
			
			os.chdir("Encryption/");

			os.chdir("Key/");

			a=os.path.abspath("");

			sys.path.append(a)
		
			from additive_encryption_key import K;
		
			K();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		additive_name();

		encryption_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");


		os.chdir("..");

		os.chdir("Additive_Cipher/");

		os.chdir("Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from additive_encryption import Encryption;

		Encryption();

	except EOFError:

		clear();


		

		NAME();


		additive_name();

		encryption_name();	

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");


		os.chdir("..");

		os.chdir("Additive_Cipher/");

		os.chdir("Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from additive_encryption import Encryption;

		Encryption();

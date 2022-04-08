def Crypt():
	
	import os;

	import sys

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from clear_function import clear;

	from program_name import NAME;

	from encryption_name import encryption_name;
	
	from decryption_name import decryption_name;

	from brute_name import brute_name;
	
	from help_name import help_name;

	from additive_name import additive_name;

	from exit_function import exit;	

	try:

		crypt=input("\033[1;32;40m"+"【1】 Encryption\n\n【2】 Decryption\n\n【3】 Brute Force\n\n【4】 Help\n\n【5】 Back\n\n【6】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if crypt=='1':

			clear();

			NAME();

			additive_name();

			encryption_name();
			
			os.chdir("..");

			os.chdir("Additive_Cipher/");			

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a)

			from additive_encryption import Encryption;
						
			Encryption();

		elif crypt=='2':

			clear();

			NAME();

			additive_name();

			decryption_name();
			
			os.chdir("..");

			os.chdir("Additive_Cipher/");			

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_decryption import Decryption;
			
			Decryption();

		elif crypt=='3':
			
			clear();

			NAME();

			additive_name();

			brute_name();
			
			os.chdir("..");

			os.chdir("Additive_Cipher/");			

			os.chdir("Brute_Force/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_brute import Brute;
			
			Brute();			

		elif crypt=="4":

			clear();

			NAME();

			additive_name();

			help_name();
			
			os.chdir("..");

			os.chdir("Additive_Cipher/");			

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_help import Help;
			
			Help();		
			
		elif crypt=="5":
		
			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			clear();

			NAME();

			from cryptestein import Cryptestein;

			Cryptestein();

		elif crypt=="6":
			exit();


		elif crypt=="":



			clear();



	
			NAME();
	

			additive_name()	

	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");




			Crypt();


		else:

			

			clear();


			
		
			NAME();
		
			additive_name()	

			
			
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+crypt+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");


			
			Crypt();

	except KeyboardInterrupt:

		

		clear();


		
	
		NAME();


		additive_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Crypt();

	except EOFError:

		

		clear();


		
				
		NAME();


		additive_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Crypt();

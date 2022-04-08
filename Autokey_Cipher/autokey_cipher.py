def Autokey():

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

	from autokey_name import autokey_name;

	from exit_function import exit;	

	try:


			

		autokey=input("\033[1;32;40m"+"① Encryption\n\n② Decryption\n\n③ Brute Force\n\n④ Help\n\n⑤ Back\n\n⑥ Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");



		if autokey=='1':

			

			clear();


			

			NAME();

			autokey_name();

			encryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");			

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a)

			from autokey_encryption import Encryption;

			Encryption();

		elif autokey=='2':
			
			

			clear();


			

			NAME();



			autokey_name();

			decryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");			

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from autokey_decryption import Decryption;
			
			Decryption();
		

		elif autokey=='3':
			
			

			clear();


			

			NAME();



			autokey_name();

			brute_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");			

			os.chdir("Brute_Force/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from autokey_brute import Brute;			

			Brute();

		elif autokey=="4":

			clear();

			NAME();

			autokey_name();

			help_name();
			
			os.chdir("..");

			os.chdir("Autokey_Cipher/");			

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);
				
			from autokey_help import Help;			
			
			Help();


		elif autokey=="5":

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			clear();

			NAME();

			from cryptestein import Cryptestein;

			Cryptestein();

		elif autokey=="6":
			exit();


		elif autokey=="":



			clear();



	
			NAME();
	

			autokey_name()	

	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");




			Autokey();


		else:

			

			clear();


			
		
			NAME();
		
			autokey_name()	

			
			
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+autokey+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");


			
			Autokey();

	except KeyboardInterrupt:

		
		clear();



		
	
		NAME();


		autokey_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Autokey();

	except EOFError:

		

		clear();


		
				
		NAME();


		autokey_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Autokey();

def Cyber():

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

	from multiplicative_name import multiplicative_name;

	from exit_function import exit;	

	try:
		cyber=input("\033[1;32;40m"+"① Encryption\n\n② Decryption\n\n③ Brute Force\n\n④ Help\n\n⑤ Back\n\n⑥ Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if cyber=='1':

			clear();

			NAME();

			multiplicative_name();

			encryption_name();
			
			os.chdir("..");

			os.chdir("Multiplicative_Cipher/");			

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a)

			from multiplicative_encryption import Encryption;

			Encryption();

		elif cyber=='2':

			clear();

			NAME();

			multiplicative_name();

			decryption_name();
			
			os.chdir("..");

			os.chdir("Multiplicative_Cipher/");			

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a)

			from multiplicative_decryption import Decryption;

			Decryption();

		elif cyber=='3':

			clear();

			NAME();

			multiplicative_name();

			brute_name();
			
			os.chdir("..");

			os.chdir("Multiplicative_Cipher/");			

			os.chdir("Brute_Force/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from multiplicative_brute import Brute;
			
			Brute();

		elif cyber=="4":

			clear();

			NAME();

			multiplicative_name();

			help_name();
			
			os.chdir("..");

			os.chdir("Multiplicative_Cipher/");			

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from multiplicative_help import Help;
			
			Help();


		elif cyber=="5":

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			clear();

			NAME();

			from cryptestein import Cryptestein;

			Cryptestein();

		elif cyber=="6":
			exit();


		elif cyber=="":



			clear();



	
			NAME();
	

			multiplicative_name()	

	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");




			Cyber();


		else:

			

			clear();


			
		
			NAME();
		
			multiplicative_name()	

			
			
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+cyber+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");


			
			Cyber();

	except KeyboardInterrupt:

		

		clear();


		
	
		NAME();


		multiplicative_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Cyber();

	except EOFError:

		

		clear();


		
				
		NAME();


		multiplicative_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Cyber();

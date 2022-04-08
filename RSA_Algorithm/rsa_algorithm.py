def RSA():

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

	from rsa_name import rsa_name;

	from private_key_name import key_name;

	from exit_function import exit;	

	try:


		
		Rsa=input("\033[1;32;40m"+"① Private Key\n\n② Encryption\n\n③ Decryption\n\n④ Help\n\n⑤ Back\n\n⑥ Exit\n\n"+"\033[1;36;40m"+"Choose an Opttion : "+"\033[0m");
		
		if Rsa=='1':

			clear();


			

			NAME();

			rsa_name();

			key_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Private_Key_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a)

			from rsa_private_key_prime1 import Prime1;
		
			Prime1();

		elif Rsa=='2':

			clear();			

			NAME();

			rsa_name();

			encryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");			

			os.chdir("RSA_Encryption_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a)

			from rsa_encryption_prime1 import Prime1;
		
			Prime1();

		elif Rsa=='3':

			clear();			

			NAME();

			rsa_name();

			decryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");			

			os.chdir("RSA_Decryption_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a)

			from rsa_decryption_prime1 import Prime1;
		
			Prime1();

		elif Rsa=="4":

			clear();

			NAME();

			rsa_name();

			help_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");			

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a)

			from rsa_help import Help;
			
			Help();


		elif Rsa=="5":

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			clear();

			NAME();

			from cryptestein import Cryptestein;

			Cryptestein();

		elif Rsa=="6":
			exit();


		elif Rsa=="":



			clear();



	
			NAME();
	

			rsa_name()	

	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");




			RSA();


		else:

			

			clear();


			
		
			NAME();
		
			rsa_name()	

			
			
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+Rsa+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");


			
			RSA();

	except KeyboardInterrupt:
	
		

		clear();


		
	
		NAME();


		rsa_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		RSA();

	except EOFError:

		

		clear();


		
				
		NAME();


		rsa_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		RSA();

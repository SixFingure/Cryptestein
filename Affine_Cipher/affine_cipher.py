def Affine():
	
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

	from affine_name import affine_name;

	from exit_function import exit;	

	try:

		affine=input("\033[1;32;40m"+"【1】 Encryption\n\n【2】 Decryption\n\n【3】 Help\n\n【4】 Back\n\n【5】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if affine=='1':

			clear();

			NAME();

			affine_name();

			encryption_name();
			
			os.chdir("..");

			os.chdir("Affine_Cipher/");			

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a)

			from affine_encryption import Encryption;
						
			Encryption();

		elif affine=='2':

			clear();

			NAME();

			affine_name();

			decryption_name();
			
			os.chdir("..");

			os.chdir("Affine_Cipher/");			

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from affine_decryption import Decryption;
			
			Decryption();

		elif affine=="3":

			clear();

			NAME();

			affine_name();

			help_name();
			
			os.chdir("..");

			os.chdir("Affine_Cipher/");			

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from affine_help import Help;
			
			Help();		
			
		elif affine=="4":
		
			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			clear();

			NAME();

			from cryptestein import Cryptestein;

			Cryptestein();

		elif affine=="5":
			exit();


		elif affine=="":



			clear();



	
			NAME();
	

			affine_name()	

	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");




			Affine();


		else:

			

			clear();


			
		
			NAME();
		
			affine_name()	

			
			
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+affine+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");


			
			Affine();

	except KeyboardInterrupt:

		

		clear();


		
	
		NAME();


		affine_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Affine();

	except EOFError:

		

		clear();


		
				
		NAME();


		affine_name()	
		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
		Affine();

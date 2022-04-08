def Help():

	import os;

	import sys

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from additive_name import additive_name;
	
	from autokey_name import autokey_name;
	
	from multiplicative_name import multiplicative_name;
	
	from rsa_name import rsa_name;

	from affine_name import affine_name;
	
	from help_name import help_name;

	from encryption_name import encryption_name;
	
	from decryption_name import decryption_name;

	from exit_function import exit;

	try:	
		help=input("\033[1;32;40m"+"【1】 Additive Cipher\n\n【2】 Multiplicative Cipher\n\n【3】 Autokey Cipher\n\n【4】 RSA Algorithm\n\n【5】 Affine Cipher\n\n【6】 Back\n\n【7】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");
		if help=="1":

			clear();

			NAME();

			help_name();
			
			additive_name();

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Additive_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from cryptestein_additive_help import Inp,text;

			text();

			Inp();


		elif help=="2":

			clear();

			NAME();

			help_name();
			
			multiplicative_name();

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Multiplicative_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from cryptestein_multiplicative_help import Inp,text;

			text();

			Inp();

		elif help=="3":
		
			clear();

			NAME();

			help_name();
			
			autokey_name();

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Autokey_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from cryptestein_autokey_help import Inp,text;

			text();

			Inp();

		elif help=="4":
			clear();

			NAME();

			help_name();

			rsa_name();

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("RSA_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from cryptestein_rsa_help import Inp,text;

			text();

			Inp();

		elif help=="5":

			clear();

			NAME();

			help_name();

			affine_name();

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Affine_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from cryptestein_affine_help import Inp,text;

			text();

			Inp();

		elif help=="6":

			clear();

			NAME();

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein import Cryptestein;

			Cryptestein();


		elif help=="7":

			exit();

		elif help=="":

			clear();

			NAME();

			help_name();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_help import Help;

			Help();									

		else:

			clear();

			NAME();

			help_name();
									
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+help+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_help import Help;

			Help();									



	except KeyboardInterrupt:

		clear();

		NAME();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_help import Help;

		Help();									

	except EOFError:

		clear();

		NAME();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_help import Help;

		Help();									

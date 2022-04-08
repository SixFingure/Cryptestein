def Help():

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from autokey_name import autokey_name;

	from encryption_name import encryption_name;
	
	from decryption_name import decryption_name;

	from help_name import help_name;

	from exit_function import exit;

	try:	

		help=input("\033[1;32;40m"+"① Encryption\n\n② Decryption\n\n③ Back\n\n④ Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if help=="1":

			clear();

			NAME();

			autokey_name();

			help_name();
			
			encryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from autokey_encryption_help import Inp,text;

			text();

			Inp();


		elif help=="2":

			clear();

			NAME();

			autokey_name();

			help_name();
			
			decryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			os.chdir("Decryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from autokey_decryption_help import Inp,text;

			text();

			Inp();

		elif help=="3":

			clear();

			NAME();

			autokey_name();

			os.chdir("..");
			
			os.chdir("Autokey_Cipher/");
			
			a=os.path.abspath("");

			sys.path.append(a);
			
			from autokey_cipher import Autokey;

			Autokey();

		elif help=="4":

			exit();

		elif help=="":

			clear();

			NAME();

			autokey_name();

			help_name();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_help import Help;

			Help();									

		else:

			clear();

			NAME();

			autokey_name();

			help_name();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+help+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_help import Help;

			Help();


	except KeyboardInterrupt:

		clear();

		NAME();

		autokey_name();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_help import Help;

		Help();

	except EOFError:

		clear();

		NAME();

		autokey_name();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_help import Help;

		Help();

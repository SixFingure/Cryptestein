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

	from rsa_name import rsa_name;

	from encryption_name import encryption_name;
	
	from decryption_name import decryption_name;

	from private_key_name import key_name;

	from help_name import help_name;

	from exit_function import exit;

	try:	

		help=input("\033[1;32;40m"+"① Private Key\n\n② Encryption\n\n③ Decryption\n\n④ Back\n\n⑤ Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if help=="1":

			clear();

			NAME();

			rsa_name();

			help_name();
			
			key_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			os.chdir("Private_Key_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from rsa_private_key_help import Inp,text;

			text();

			Inp();

		elif help=="2":

			clear();

			NAME();

			rsa_name();

			help_name();
			
			encryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from rsa_encryption_help import Inp,text;

			text();

			Inp();

		elif help=="3":

			clear();

			NAME();

			rsa_name();

			help_name();
			
			decryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			os.chdir("Decryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from rsa_decryption_help import Inp,text;

			text();
			
			Inp();

		elif help=="4":

			clear();

			NAME();

			rsa_name();

			os.chdir("..");
			
			os.chdir("RSA_Algorithm/");
			
			a=os.path.abspath("");

			sys.path.append(a);
			
			from rsa_algorithm import RSA;
			
			RSA();

		elif help=="5":

			exit();

		elif help=="":

			clear();

			NAME();

			rsa_name();

			help_name();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_help import Help;

			Help();									

		else:

			clear();

			NAME();

			rsa_name();

			help_name();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+help+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_help import Help;

			Help();


	except KeyboardInterrupt:

		clear();

		NAME();

		rsa_name();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_help import Help;

		Help();

	except EOFError:

		clear();

		NAME();

		rsa_name();

		help_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_help import Help;

		Help();

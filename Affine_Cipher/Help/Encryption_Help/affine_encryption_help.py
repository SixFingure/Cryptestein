def text():

	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Encryption, first the plain text is encrypted using Multiplicative Cipher and then again encrypted using affine Cipher.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"The value of Key can only be from 0 to 25.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Example :\n\n\tPlain Text = "'"abxy"'"\n\n\tKey1 = 5\n\n\tKey2 = 17\n\n\tEncrypted Text= "'"RWCH"'"\n"+"\033[0m");

def Inp():

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from affine_name import affine_name;

	from encryption_name import encryption_name;

	from help_name import help_name;

	from exit_function import exit;

	try:

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if inp=="1":

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

		elif inp=="2":

			exit();

		elif inp=="":

			clear();

			NAME();

			affine_name();

			help_name();

			encryption_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_help import Inp;

			Inp();									

		else:

			clear();

			NAME();

			affine_name();

			help_name();

			encryption_name();
				
			text();				
	
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_help import Inp;

			Inp();

	except KeyboardInterrupt:

		clear();

		NAME();

		affine_name();

		help_name();

		encryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Help/");

		os.chdir("Encryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_help import Inp;

		Inp();

	except EOFError:

		clear();

		NAME();

		affine_name();

		help_name();

		encryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Help/");

		os.chdir("Encryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_help import Inp;

		Inp();

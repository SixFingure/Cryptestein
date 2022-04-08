def text():

	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Decryption, the First Letter of Plain Text is obtained by Subtracting the Autokey from the First Letter of Encrypted Text, then the Second Letter of Plain Text is obtained by Subtracting the First letter of Plain Text from the Second Letter of Encrypted Text and so on.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"The value of Autokey can only be from 0 to 25.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Example :\n\n\tEncrypted Text = "'"FBYV"'"\n\n\tKey = 5\n\n\tPlain Text = "'"abxy"'"\n"+"\033[0m");

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

	from autokey_name import autokey_name;

	from decryption_name import decryption_name;

	from help_name import help_name;

	from exit_function import exit;

	try:

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if inp=="1":

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


		elif inp=="2":

			exit();

		elif inp=="":

			clear();

			NAME();

			autokey_name();

			help_name();

			decryption_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			os.chdir("Decryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_decryption_help import Inp;

			Inp();									

		else:

			clear();

			NAME();

			autokey_name();

			help_name();

			decryption_name();

			text();
					
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Help/");

			os.chdir("Decryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_decryption_help import Inp;

			Inp();

	except KeyboardInterrupt:

		clear();

		NAME();

		autokey_name();

		help_name();

		decryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Help/");

		os.chdir("Decryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_decryption_help import Inp;

		Inp();

	except EOFError:

		clear();

		NAME();

		autokey_name();

		help_name();

		decryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Help/");

		os.chdir("Decryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_decryption_help import Inp;

		Inp();

def text():
	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Encryption each Character of Plain Text is First Multiplied by the value of Key and then Product of Character and Key is then Modulo by 26.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Decryption each Character of Encrypted Text is First Multiplied by the Modular Inverse of the value of Key and then Product of Character and Modular Inverse of Key is then Modulo by 26.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"The value of Key has to be choosen such that the GCD of Key and 26 will be Equal to 1.\n");

def Inp():

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from multiplicative_name import multiplicative_name;

	from help_name import help_name;

	from exit_function import exit;

	try:

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if inp=="1":

			clear();


				

			NAME();

			help_name();

			os.chdir("..");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_help import Help;

			Help();


		elif inp=="2":

			exit();

		elif inp=="":

			clear();

			NAME();

			help_name();

			multiplicative_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Multiplicative_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_multiplicative_help import Inp;

			Inp();									

		else:

			clear();

			NAME();

			help_name();

			multiplicative_name();

			text();
				
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Multiplicative_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_multiplicative_help import Inp;

			Inp();									

	except KeyboardInterrupt:

		clear();

		NAME();

		help_name();	

		multiplicative_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("Multiplicative_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_multiplicative_help import Inp;

		Inp();									
		
	except EOFError:

		clear();

		NAME();

		help_name();

		multiplicative_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("Multiplicative_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_multiplicative_help import Inp;

		Inp();									

def text():
	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"RSA Algorithm is Asymmetric Cryptography Algorithm.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Asymmetric means that it works on two different keys i.e. Public Key and Private Key.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Public Key is given to Everyone and Private Key is kept Private.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Encryption and Decryption, two Prime numbers and a Public Key is selected and then from these three values Private Key is generated and then by the user of Public Key and Private Key Plain Text is Encrypted and Encrypted Text is Decrypted.\n");

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

	from rsa_name import rsa_name;

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

			rsa_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("RSA_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_rsa_help import Inp;

			Inp();									

		else:

			clear();

			NAME();

			help_name();

			rsa_name();

			text();
				
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("RSA_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_rsa_help import Inp;

			Inp();									

	except KeyboardInterrupt:

		clear();

		NAME();

		help_name();

		rsa_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("RSA_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_rsa_help import Inp;

		Inp();									

	except EOFError:

		clear();

		NAME();

		help_name();

		rsa_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("RSA_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_rsa_help import Inp;

		Inp();									

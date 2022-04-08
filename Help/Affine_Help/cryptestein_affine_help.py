def text():
	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Affine Cipher is a mixture of Additive Cipher and Multiplicative Cipher.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Encryption, first the plain text is encrypted using Multiplicative Cipher and then again encrypted using Additive Cipher.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Decryption, the encrypted text is first decrypted using Additive Cipher and then again decrypted using Multiplicative Cipher.\n");

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

	from affine_name import affine_name;

	from help_name import help_name;

	from exit_function import exit;


	try:

		inp=input("\033[1;32;40m"+"【1】 Back\n\n【2】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

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

			affine_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Affine_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_affine_help import Inp;

			Inp();									

		else:

			clear();

			NAME();

			help_name();

			affine_name();

			text();
				
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Help/");

			os.chdir("Affine_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein_affine_help import Inp;

			Inp();									

	except KeyboardInterrupt:

		clear();

		NAME();

		help_name();

		affine_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("Affine_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_affine_help import Inp;

		Inp();									

	except EOFError:

		clear();

		NAME();

		help_name();

		affine_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Help/");

		os.chdir("Affine_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein_affine_help import Inp;

		Inp();									

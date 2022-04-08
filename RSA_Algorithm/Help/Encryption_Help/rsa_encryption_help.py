def text():

	print("\033[1;34;40m"+"○ "+"\033[1;35;40m"+"In Encryption we first find the Private Key.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"To find Private Key, two Prime Numbers which are different from each other are entered and a Public Key is also provided by the User.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"n is calculated by Multiplying First and Second Prime Numbers.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"φ(n) or phie_n is calculated such that gcd(Public Key, φ(n)) has to be 1 by using formula '"'φ(n) = (First Prime − 1) × (Second Prime − 1)'"'.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Private Key is now calculated by using formula '"'Public Key × Private Key = 1 (mod φ(n))'"'.\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Now, the user enters the Plain Text\n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Now, each letter of Plain Text is converted into Encrypted Text one by one by using the formula '"'Encrypted Character = (Plain Character^Public Key)*(mod n)'"' \n\n"+"\033[1;34;40m"+"○ "+"\033[1;35;40m"+"Example :\n\n\t1st Prime = 11\n\n\t2nd Prime = 13\n\n\tPublic Key = 23\n\n\tn = 143\n\n\tφ(n) = 120\n\n\tPrivate Key = 47\n\n\tPlain Text = "'"abxy"'"\n\n\tEncrypted Text = "'"0,1,56,19"'"\n"+"\033[0m");

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

	from rsa_name import rsa_name;

	from encryption_name import encryption_name;

	from help_name import help_name;

	from exit_function import exit;

	try:

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if inp=="1":

			clear();


			NAME();

			rsa_name();

			help_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_help import Help;

			Help();

		elif inp=="2":

			exit();

		elif inp=="":

			clear();

			NAME();

			rsa_name();

			help_name();

			encryption_name();

			text();

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_help import Inp;

			Inp();									
			
		else:

			clear();

			NAME();

			rsa_name();

			help_name();

			encryption_name();

			text();
					
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+inp+'"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("Help/");

			os.chdir("Encryption_Help/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_help import Inp;

			Inp();									

	except KeyboardInterrupt:

		clear();

		NAME();

		rsa_name();

		help_name();

		encryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("Help/");

		os.chdir("Encryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption_help import Inp;

		Inp();									
	except EOFError:

		clear();

		NAME();

		rsa_name();

		help_name();

		encryption_name();

		text();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("Help/");

		os.chdir("Encryption_Help/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption_help import Inp;

		Inp();		

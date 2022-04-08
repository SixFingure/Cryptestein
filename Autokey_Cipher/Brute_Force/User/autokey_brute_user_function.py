def User():

	import os;

	import sys

	a=os.path.abspath("");

	sys.path.append(a);

	os.chdir("..");

	os.chdir("Autokey_Cipher/");

	os.chdir("Brute_Force/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from autokey_brute import inp;
	
	from autokey_brute import key_lst;

	from autokey_brute import decrypted_word_lst;

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from exit_function import exit;

	from autokey_name import autokey_name;
	
	from brute_name import brute_name;

	try:
		user=input("\033[1;32;40m"+"① Continue\n\n② Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");

		if user=="1":
		
			clear();

			NAME();

			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a)

			from cryptestein import Cryptestein;

			Cryptestein();
	
		elif user=="2":
			exit();
		
		elif user=="":
			clear();
			NAME();
			autokey_name();
			brute_name();
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+"\033[1;35;40m"+'"'+inp+'"\n'); 
			for i in range(len(decrypted_word_lst)):
				print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+"{}".format(key_lst[i])+'" '+"\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word_lst[i]+'"\n');
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n"+"\033[0m");			
			User();

		else:
			clear();
			NAME();
			autokey_name();
			brute_name();			
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+"\033[1;35;40m"+'"'+inp+'"\n'); 
			for i in range(len(decrypted_word_lst)):
				print("\033[1;34;40m"+"key : "+"\033[1;35;40m"+'"'+"{}".format(key_lst[i])+'" '+"\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word_lst[i]+'"\n');
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n"+"\033[0m");			
			User();
																
	except KeyboardInterrupt:

		clear();


		

		NAME();


		autokey_name();
		brute_name();
		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+"\033[1;35;40m"+'"'+inp+'"\n'); 
		for i in range(len(decrypted_word_lst)):
			print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+"{}".format(key_lst[i])+'" '+"\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word_lst[i]+'"\n');
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

	except EOFError:

		clear();


		

		NAME();


		autokey_name();
		brute_name();
		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+"\033[1;35;40m"+'"'+inp+'"\n'); 
		for i in range(len(decrypted_word_lst)):
			print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+"{}".format(key_lst[i])+'" '+"\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word_lst[i]+'"\n');
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

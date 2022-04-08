def User():

	import os;

	import sys

	os.chdir("..");

	os.chdir("RSA_Algorithm/");
	
	os.chdir("RSA_Decryption_Prime1/");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_decryption_prime1 import prime1;
	
	os.chdir("RSA_Decryption_Prime2/");
	
	a=os.path.abspath("");

	sys.path.append(a);
	
	from rsa_decryption_prime2 import prime2;

	os.chdir("RSA_Public_Key_For_Decryption/");
	
	a=os.path.abspath("");

	sys.path.append(a);
	
	from rsa_public_key_for_decryption import e,d;
	
	os.chdir("Decryption/");
	
	a=os.path.abspath("");

	sys.path.append(a);
	
	from rsa_decryption import decrypted_word,inp;	

	os.chdir("..");

	os.chdir("..");
	
	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from exit_function import exit;

	from rsa_name import rsa_name;
	
	from decryption_name import decryption_name;

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
			rsa_name();
			decryption_name();
			print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");

			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'", you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
			User();

		else:
			clear();
			NAME();
			rsa_name();
			decryption_name();			
			print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");

			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+user+'",',"which contains unacceptable characters\n"+"\033[0m");			
			User();
																
	except KeyboardInterrupt:

		clear();


		

		NAME();


		rsa_name();
		decryption_name();
		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

	except EOFError:

		clear();


		

		NAME();


		rsa_name();
		decryption_name();
		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"'\n"+"\033[0m");
		User();

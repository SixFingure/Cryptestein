inp="";

encrypted_word="";
def Encryption():	

	import os;

	import sys

	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_encryption_user_function import User;
	
	os.chdir("..");	

	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_public_key_for_encryption import e,d;

	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_encryption_prime2 import prime2,n;
	
	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_encryption_prime1 import prime1;

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;
	
	from program_name import NAME;
	
	from rsa_name import rsa_name;

	from encryption_name import encryption_name;

	from exit_function import exit;

	try:

		global inp;

		global encrypted_word;

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Enter the Text you want to Encrypt in Small Alphabets Only : "+"\033[0m");

		clear();




		NAME();

		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

		if inp=="1":

			clear();


	

			NAME();

			rsa_name();

			encryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_public_key_for_encryption import E;
			
			print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m");			
						
			E();

		elif inp=="2":

			exit();

		elif inp=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Encryption/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption import Encryption;

			Encryption();


		char=False;					
		ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]
		for c in inp:

			if c.isdigit() or c.isupper():

				char=True;
				break;

			elif c==chr(92):
				char=True;
				break;

			else:
				for i in ls:
					if i==c:

						char=True;
						break;



		if char==True:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Encryption/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption import Encryption;

			Encryption();

		else:

			index=[];
			for i in inp:
				if i==" ":
					index.append(32);
				else:
					index.append(ord(i)-97);

			C=[];
			for i in index:

				if i==32:
					C.append(int(i));

				else:
					c=(int(i)**int(e))%n;
					C.append(c);

			encrypt_word=[];
			for i in C:
				if i==32:
					encrypt_word.append(chr(32));
				else:				
					encrypt_word.append(i);
			
			encrypted_word="";

			for encrypt_letter in encrypt_word:
				encrypted_word=encrypted_word+"{}".format(encrypt_letter)+",";
			encrypted_word=encrypted_word[:-1];																						

			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+encrypted_word+'"\n'+"\033[0m");

			User();

	except KeyboardInterrupt:

		clear();

		NAME();

		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 
		
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Encryption/");

		os.chdir("Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption import Encryption;

		Encryption();

	except EOFError:

		clear();

		NAME();

		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 
		
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Encryption/");

		os.chdir("Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption import Encryption;

		Encryption();

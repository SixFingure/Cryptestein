inp="";

decrypted_word="";

def Decryption():	

	import os;

	import sys

	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_decryption_user_function import User;
	
	os.chdir("..");	

	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_public_key_for_decryption import e,d;

	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_decryption_prime2 import prime2,n;
	
	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);

	from rsa_decryption_prime1 import prime1;

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;
	
	from program_name import NAME;
	
	from rsa_name import rsa_name;

	from decryption_name import decryption_name;

	from exit_function import exit;

	try:

		global inp;

		global decrypted_word;

		inp=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter the Text you want to Decrypt in Numbers or Spaces, Separated with Commas only : "+"\033[0m");

		clear();




		NAME();

		rsa_name();

		decryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

		if inp=="A":

			clear();


	

			NAME();

			rsa_name();

			decryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Decryption_Prime1/");

			os.chdir("RSA_Decryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_public_key_for_decryption import E;
			
			print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

			print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m");			
						
			E();

		elif inp=="B":

			exit();

		elif inp=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'𝓐'"' or '"'𝓑'"' or should have Entered Text you want to Decrypt in Numbers or Spaces, Separated with Commas only\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Decryption_Prime1/");

			os.chdir("RSA_Decryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Decryption/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_decryption import Decryption;

			Decryption();



		char=False;					
		ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`","]"]
		for c in inp:

			if c.isalpha():

				char=True;

			elif c==chr(92):
				char=True;

			else:
				for i in ls:
					if i==c:

						char=True;




		if char==True:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered","'"+c+"'","along with the Text\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Decryption_Prime1/");

			os.chdir("RSA_Decryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Decryption/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_decryption import Decryption;

			Decryption();


		else:

			characters=inp.split(",");
									
			index=[];
			for i in characters:
				if i==" "*len(i):
					for i in range(len(i)):
						index.append(32);
				else:
					index.append(i);

			for i in index:
				if i=="":
					print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"At somewhere in the encrypted text, you entered consicutive commas and there was no number or space between them\n"+"\033[0m");
					os.chdir("..");

					os.chdir("RSA_Algorithm/");

					os.chdir("RSA_Decryption_Prime1/");

					os.chdir("RSA_Decryption_Prime2/");

					os.chdir("RSA_Public_Key_For_Decryption/");

					os.chdir("Decryption/");

					a=os.path.abspath("");

					sys.path.append(a);

					from rsa_decryption import Decryption;

					Decryption();
			M=[];
			for i in index:

				if i==32:
					M.append(int(i));

				else:
					m=(int(i)**int(d))%n;
					M.append(m);

			decrypt_num=0;
			decrypt_word=[];
			for i in M:
				if i==32:
					decrypt_word.append(chr(32));
				else:				
					decrypt_num=97+i;
					decrypt_word.append(chr(decrypt_num));
					decrypt_num=0;
			
			decrypted_word="";
			for decrypt_letter in decrypt_word:
				decrypted_word=decrypted_word+decrypt_letter;															
			
			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m");
	
			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");

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
		
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Decryption_Prime1/");

		os.chdir("RSA_Decryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Decryption/");

		os.chdir("Decryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_decryption import Decryption;

		Decryption();

	except EOFError:

		clear();

		NAME();

		rsa_name();

		decryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 
		
		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Small Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Decryption_Prime1/");

		os.chdir("RSA_Decryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Decryption/");

		os.chdir("Decryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_decryption import Decryption;

		Decryption();

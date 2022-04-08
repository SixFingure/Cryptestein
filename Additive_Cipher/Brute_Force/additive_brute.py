inp="";

decrypted_word_lst=[];

key_lst=[];

def Brute():
	
	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from brute_name import brute_name;
	
	from decryption_name import decryption_name;
	
	from help_name import help_name;

	from additive_name import additive_name;

	from exit_function import exit;
		
	os.chdir("..");

	os.chdir("Additive_Cipher/");

	os.chdir("Brute_Force/");

	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);	

	from additive_brute_user_function import User;

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	try:

		global inp;

		inp=input("\033[1;32;40m"+"① Back\n\n② Exit\n\n"+"\033[1;36;40m"+"Enter the Text you want to Decrypt in Capital Alphabets Only : "+"\033[0m");

		clear();

		NAME();

		additive_name();

		brute_name();

		if inp=="1":

			clear();

			NAME();

			additive_name();

			os.chdir("..");
			
			os.chdir("Additive_Cipher/");
			
			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_cipher import Crypt;
			
			Crypt();

		elif inp=="2":

			exit();

		elif inp=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Additive_Cipher/");

			os.chdir("Brute_Force/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_brute import Brute;

			Brute();
			
		char=False;			
		
		ls=["[","@",";","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]

		for c in inp:

			if c.isdigit() or c.islower():

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

			os.chdir("Additive_Cipher/");

			os.chdir("Brute_Force/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from additive_brute import Brute;

			Brute();

		else:
		
			global decrypted_word_lst;
			
			global key_lst;

			decrypted_word_lst=[];
			
			key_lst=[];

			clear();

			NAME();

			additive_name();

			brute_name();

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+"\033[1;35;40m"+'"'+inp+'"\n'); 

			index=[];
			for i in inp:
				if i==" ":
					index.append(32);
				else:
					index.append(ord(i)-65);
					
			decrypt_val=[];
			start=0;
			for key in range(0,26):
				for den_val in index:

					if den_val==32:
						decrypt_val.append(32);
						start=start+1;

					else:
						a=int(index[start])-int(key);
						if a<0:
							a=a+26;
							m=a%26;
							decrypt_val.append(m);
							start=start+1;

						else:
							m=a%26;
							decrypt_val.append(m);
							start=start+1;
						
					decrypt_num=0;
					decrypt_word=[];
					for i in decrypt_val:
						if i==32:
							decrypt_word.append(chr(32));		
						else:				
							decrypt_num=97+i;
							decrypt_word.append(chr(decrypt_num));
							decrypt_num=0;
						
					decrypted_word="";
					for decrypt_letter in decrypt_word:
						decrypted_word=decrypted_word+decrypt_letter;


				print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+"{}".format(key)+'" '+"\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n');

				decrypted_word_lst.append(decrypted_word);
				
				key_lst.append(key);

				decrypt_val=[];
				start=0;

			User();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		additive_name();

		brute_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Additive_Cipher/");

		os.chdir("Brute_Force/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from additive_brute import Brute;

		Brute();

	except EOFError:

		clear();


		

		NAME();



		additive_name();

		brute_name();	

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Additive_Cipher/");

		os.chdir("Brute_Force/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from additive_brute import Brute;

		Brute();

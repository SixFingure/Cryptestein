key_reserve="";
decrypted_word="";

def K(): 
	
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

	from exit_function import exit;

	os.chdir("..");

	os.chdir("Autokey_Cipher/");

	os.chdir("Decryption/");

	a=os.path.abspath("");

	sys.path.append(a);

	from autokey_decryption import inp;

	os.chdir("Key/");
	
	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from autokey_decryption_user_function import User;

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
		
	try:

		global decrypted_word;

		global key_reserve;

		key=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");




		clear();




		NAME();


		autokey_name();

		decryption_name();

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		if key=="A":
			
			clear();


	

			NAME();

			autokey_name();

			decryption_name();

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_decryption import Decryption;

			Decryption();

		elif key=="B":
			exit();	

		elif key=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_decryption_key import K;

			K();




		k=True;

		if key.isdigit()!=True:
			k=False

		elif int(key)>25:
			k=False

		elif int(key)<0:
			k=False



		if k==False:
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered "+'"'+key+'"'+" which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Autokey_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key/");

			a=os.path.abspath("");

			sys.path.append(a);

			from autokey_decryption_key import K;



			K();
		


		
		else:

			key_reserve=key;

			print("\033[1;34;40m"+"Key : "+"\033[1;35;40m"+'"'+key+'"\n'+"\033[0m");


			index=[];
			space=[i for i in range(len(inp)) if inp[i]==" "];

			for i in inp:
				if i==" ":
					pass;
				else:
					index.append(ord(i)-65);

			key_list=[int(key)];
			for i in index:
				key=i-int(key);
				if key<0:
					key=26+key;
					key_list.append(key);
				else:
					key_list.append(key);

			decrypt_val=[];
			start=0;
			for den_val in index:
				a=int(index[start])-key_list[start];
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
				decrypt_num=97+i;
				decrypt_word.append(chr(decrypt_num));
				decrypt_num=0;

			for i in space:
				decrypt_word.insert(i," ");
			
			decrypted_word="";
			for decrypt_letter in decrypt_word:
				decrypted_word=decrypted_word+decrypt_letter;
			
			print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");

			User();


	except KeyboardInterrupt:

		clear();


		

		NAME();



		autokey_name();

		decryption_name();	

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 


		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_decryption_key import K;

		K();

	except EOFError:

		clear();


		

		NAME();



		autokey_name();

		decryption_name();	

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 


		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Autokey_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key/");

		a=os.path.abspath("");

		sys.path.append(a);

		from autokey_decryption_key import K;

		K();

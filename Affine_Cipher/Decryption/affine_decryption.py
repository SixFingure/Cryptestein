inp="";

def Decryption():	

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from decryption_name import decryption_name;

	from affine_name import affine_name;

	from exit_function import exit;

	from help_name import help_name;
	
	try:


		global inp;

		inp=input("\033[1;32;40m"+"【1】 Back\n\n【2】 Exit\n\n"+"\033[1;36;40m"+"Enter the Text you want to Decrypt in Capital Alphabets Only : "+"\033[0m");





		clear();




		NAME();

		affine_name();

		decryption_name();

		if inp=="1":

			clear();

			NAME();

			affine_name();

			os.chdir("..");
			
			os.chdir("Affine_Cipher/");
			
			a=os.path.abspath("");

			sys.path.append(a);
			
			from affine_cipher import Affine;
			
			Affine();
	
		elif inp=="2":

			exit();

		elif inp=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from affine_decryption import Decryption;

			Decryption();


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

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);
			
			from affine_decryption import Decryption;


			Decryption();

		


		else:

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

			os.chdir("..");

			os.chdir("Affine_Cipher/");
			
			os.chdir("Decryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a)
		
			from affine_decryption_key1 import K1;
		
			K1();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		affine_name();

		decryption_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from affine_decryption import Decryption;

		Decryption();

	except EOFError:

		clear();


		

		NAME();



		affine_name();

		decryption_name();	

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or should have Entered text in Capital Alphabets\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		a=os.path.abspath("");

		sys.path.append(a);
		
		from affine_decryption import Decryption;

		Decryption();

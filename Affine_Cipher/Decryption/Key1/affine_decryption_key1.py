key1="";
decrypt_val1="";

def K1(): 

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

	from affine_name import affine_name;

	from decryption_name import decryption_name;

	from exit_function import exit;

	os.chdir("..");

	os.chdir("Affine_Cipher/");

	os.chdir("Decryption/");

	a=os.path.abspath("");

	sys.path.append(a);

	from affine_decryption import inp;

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
		
	try:

		global key1;

		key1=input("\033[1;32;40m"+"【A】 Back\n\n【B】 Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");




		clear();




		NAME();


		affine_name();

		decryption_name();

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		if key1=="A":
			
			clear();


	

			NAME();

			affine_name();

			decryption_name();

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption import Decryption;

			Decryption();

		elif key1=="B":
			exit();	

		elif key1=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key1 import K1;

			K1();




		k=True;

		if key1.isdigit()!=True:
			k=False

		elif int(key1)>25:
			k=False

		elif int(key1)<0:
			k=False



		if k==False:
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered "+'"'+key1+'"'+" which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key1 import K1;




			K1();
		


		
		else:

			index=[];
			for i in inp:
				if i==" ":
					index.append(32);
				else:
					index.append(ord(i)-65);

			global decrypt_val1;

			decrypt_val1=[];
			start=0;
			for den_val in index:
				if den_val==32:
					decrypt_val1.append(32);
					start=start+1;
				else:				
					a=int(index[start])-int(key1);
					if a<0:
						a=a+26;
						m=a%26;
						decrypt_val1.append(m);
						start=start+1;
					else:
						m=a%26;
						decrypt_val1.append(m);
						start=start+1;
			
			print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			os.chdir("Key2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key2 import K2;

			K2();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		affine_name();

		decryption_name();	

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 


		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_decryption_key1 import K1;

		K1();

	except EOFError:

		clear();


		

		NAME();



		affine_name();

		decryption_name();	

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_decryption_key1 import K1;

		K1();

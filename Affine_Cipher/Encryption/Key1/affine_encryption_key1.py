key1="";

encrypt_val1="";

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

	from encryption_name import encryption_name;

	from exit_function import exit;

	os.chdir("..");

	os.chdir("Affine_Cipher/");

	os.chdir("Encryption/");

	a=os.path.abspath("");

	sys.path.append(a);

	from affine_encryption import inp;

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	try:

		global key1;

		key1=input("\033[1;32;40m"+"【A】 Back\n\n【B】 Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key for Multiplicative Encryption in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");

		clear();

		NAME();

		affine_name();

		encryption_name();

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 
		
		if key1=="A":
			
			clear();

			NAME();

			affine_name();

			encryption_name();

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption import Encryption;

			Encryption();

		elif key1=="B":
			exit();	

		elif key1=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_key1 import K1;

			K1();

		k=True;

		if key1.isdigit()!=True:
			k=False

		elif int(key1)>25:
			k=False

		elif int(key1)<0:
			k=False



		if k==False:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered",'"'+key1+'",',"which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Encryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_encryption_key1 import K1;

			K1();
		



		else:

			index=[];
			for i in inp:
				if i==" ":
					index.append(32);
				else:
					index.append(ord(i)-97);

			if int(key1)==0:
				gcd=26;

			if int(key1)>26:
				smaller=26;
			
			else:
				smaller=int(key1);
			for i in range(1,smaller+1):

				if((int(key1)%i==0)and(26%i==0)):
					gcd=i;
			if gcd==1:
				
				global encrypt_val1;

				encrypt_val1=[];
				start=0;
				for en_val in index:
					if en_val==32:
						encrypt_val1.append(32);
						start=start+1;
					else:				
						encrypt_val1.append((int(index[start])*int(key1))%26);
						start=start+1;

				print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

				os.chdir("..");

				os.chdir("Affine_Cipher/");

				os.chdir("Encryption/");

				os.chdir("Key1/");

				os.chdir("Key2/");

				a=os.path.abspath("");

				sys.path.append(a);

				from affine_encryption_key2 import K2;

				K2();

			else:
				print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"Multiplicative Inverse does not exists at key =",key1,"\n"+"\033[0m");

				os.chdir("..");

				os.chdir("Affine_Cipher/");

				os.chdir("Encryption/");

				os.chdir("Key1/");

				a=os.path.abspath("");

				sys.path.append(a);

				from affine_encryption_key1 import K1;

				K1();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		affine_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_key1 import K1;

		K1();

	except EOFError:

		clear();


		

		NAME();



		affine_name();

		encryption_name();	

		print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Encryption/");

		os.chdir("Key1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_encryption_key1 import K1;

		K1();

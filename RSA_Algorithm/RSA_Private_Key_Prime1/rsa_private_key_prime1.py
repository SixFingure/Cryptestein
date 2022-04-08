prime1="";

def Prime1():

	import os;

	import sys

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from clear_function import clear;

	from program_name import NAME;

	from rsa_name import rsa_name;
	
	from private_key_name import key_name;

	from exit_function import exit;	

	try:
		global prime1;
		
		prime1=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter First Prime Number : "+"\033[0m");

		clear();

		NAME();

		rsa_name();

		key_name();

		if prime1=="A":

			clear();




			NAME();

			rsa_name();
			
			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_algorithm import RSA;

			RSA();

		elif prime1=="B":

			exit();

		elif prime1=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Private_Key_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_private_key_prime1 import Prime1;

			Prime1();

		char=False;
		ls=["[","@","_","!","#","$","%","^","&","*","(",")","<",">",'"',"'","-","?","/","|","}","{","~"," ","+",";",":",".","=","-","`",",","]"]								

		for c in prime1:

			if c.isalpha():

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
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime1+'"',"is not a Prime Number\n"+"\033[0m");	

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Private_Key_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_private_key_prime1 import Prime1;

			Prime1();
		else:
			if int(prime1)>1:
				
				for i in range(2,int(prime1)):

					if int(prime1)%i==0:
						print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime1+'"',"is not a Prime Number\n"+"\033[0m");	

						os.chdir("..");

						os.chdir("RSA_Algorithm/");

						os.chdir("RSA_Private_Key_Prime1/");

						a=os.path.abspath("");

						sys.path.append(a);

						from rsa_private_key_prime1 import Prime1;

						Prime1();

						break;

				else:

					print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

					os.chdir("..");

					os.chdir("RSA_Algorithm/");

					os.chdir("RSA_Private_Key_Prime1/");

					os.chdir("RSA_Private_Key_Prime2/");

					a=os.path.abspath("");

					sys.path.append(a);

					from rsa_private_key_prime2 import Prime2;

					Prime2();
			else:
				print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime1+'"',"is not a Prime Number\n"+"\033[0m");	

				os.chdir("..");

				os.chdir("RSA_Algorithm/");

				os.chdir("RSA_Private_Key_Prime1/");

				a=os.path.abspath("");

				sys.path.append(a);

				from rsa_private_key_prime1 import Prime1;

				Prime1();
	except KeyboardInterrupt:

		clear();


		

		NAME();



		rsa_name();

		key_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Private_Key_Prime1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_private_key_prime1 import Prime1;

		Prime1();

	except EOFError:

		clear();


		

		NAME();



		rsa_name();

		key_name();

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Private_Key_Prime1/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_private_key_prime1 import Prime1;

		Prime1();

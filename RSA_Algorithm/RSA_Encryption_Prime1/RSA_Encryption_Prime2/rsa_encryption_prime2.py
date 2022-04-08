prime2="";

phie_n="";

n="";
def Prime2():

	import os;

	import sys

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

		global prime2;

		global phie_n;
		
		global n;

		prime2=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter Second Prime Number which is different from first prime number you entered : "+"\033[0m");

		clear();




		NAME();

		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		if prime2=="A":

			clear();




			NAME();

			rsa_name();

			encryption_name();
						
			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_prime1 import Prime1;

			Prime1();


		elif prime2=="B":

			exit();

		elif prime2=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number different from first Prime Number\n"+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_prime2 import Prime2;

			Prime2();


		char=False;
		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

		for c in prime2:

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
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime2+'"',"is not a Prime Number\n"+"\033[0m");	

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_prime2 import Prime2;

			Prime2();

		if int(prime2)!=int(prime1):

			if int(prime2)>1:
				for i in range(2,int(prime2)):

					if int(prime2)%i==0:

						print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime2+'"',"is not a Prime Number\n"+"\033[0m");	

						os.chdir("..");

						os.chdir("RSA_Algorithm/");

						os.chdir("RSA_Encryption_Prime1/");

						os.chdir("RSA_Encryption_Prime2/");

						a=os.path.abspath("");

						sys.path.append(a);

						from rsa_encryption_prime2 import Prime2;

						Prime2();

				else:

					print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

					n=int(prime1)*int(prime2);

					phie_n=(int(prime1)-1)*(int(prime2)-1);

					os.chdir("..");

					os.chdir("RSA_Algorithm/");

					os.chdir("RSA_Encryption_Prime1/");

					os.chdir("RSA_Encryption_Prime2/");

					os.chdir("RSA_Public_Key_For_Encryption/");

					a=os.path.abspath("");

					sys.path.append(a);

					from rsa_public_key_for_encryption import E;

					E();

			else:

				print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime2+'"',"is not a Prime Number\n"+"\033[0m");	

				os.chdir("..");

				os.chdir("RSA_Algorithm/");

				os.chdir("RSA_Encryption_Prime1/");

				os.chdir("RSA_Encryption_Prime2/");

				a=os.path.abspath("");

				sys.path.append(a);

				from rsa_encryption_prime2 import Prime2;

				Prime2();
		else:

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+prime2+'"',"is equal to the First Prime Number you Entered\n"+"\033[0m");	

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_prime2 import Prime2;

			Prime2();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number different from first Prime Number\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption_prime2 import Prime2;

		Prime2();
	except EOFError:

		clear();


		

		NAME();



		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Prime Number different from first Prime Number\n"+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_encryption_prime2 import Prime2;

		Prime2();

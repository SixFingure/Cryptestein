e="";
d="";
def E():

	import os;

	import sys

	os.chdir("..");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from rsa_encryption_prime2 import prime2;

	from rsa_encryption_prime2 import phie_n;
	
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

		global e;
		
		global d;

		e=input("\033[1;32;40m"+"(A) Back\n\n(B) Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Public Key which is Greater Than 1 and Less Than {} : ".format(phie_n)+"\033[0m");

		clear();




		NAME();

		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		if e=="A":

			clear();




			NAME();

			rsa_name();

			encryption_name();

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_encryption_prime2 import Prime2;

			print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

			Prime2();


		elif e=="B":

			exit();

		elif e=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Number for Public Key which is Greater Than 1 and Less Than {}\n".format(phie_n)+"\033[0m");

			os.chdir("..");

			os.chdir("RSA_Algorithm/");

			os.chdir("RSA_Encryption_Prime1/");

			os.chdir("RSA_Encryption_Prime2/");

			os.chdir("RSA_Public_Key_For_Encryption/");

			a=os.path.abspath("");

			sys.path.append(a);

			from rsa_public_key_for_encryption import E;

			E();

		char=False;
		ls=["[","@","_","!","#","$","%","^","&","*","(",")"," ","<",">",";",'"',"'","-","?","/","|","}","{","~","+",":",".","=","-","`",",","]"]								

		for c in e:

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
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+'"'+e+'"',"is not a Valid Public Key\n"+"\033[0m");	

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
			if int(e)>1 and int(e)<phie_n:
				if int(e)>phie_n:
					smaller=phie_n;

				else:
					smaller=int(e);

				for i in range(1,smaller+1):
					if (int(e) % i == 0) and (phie_n % i == 0):
						gcd=i;
			
				if gcd!=1:
				
					print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"The GCD of "+e+" and {}".format(phie_n)+" is not equal to 1\n"+"\033[0m");

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

					i=1;
					while True:
						if (phie_n*i+1)%int(e)==0:
							d=(phie_n*i+1)//int(e);
							break;
						else:
							i=i+1;

					print("\033[1;34;40m"+"Public Key : "+"\033[1;35;40m"+'"'+str(e)+'"\n'+"\033[0m"); 

					print("\033[1;34;40m"+"Private Key : "+"\033[1;35;40m"+'"'+str(d)+'"\n'+"\033[0m"); 

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
				print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not entered the value between 1 and",phie_n,"\n"+"\033[0m");

				os.chdir("..");

				os.chdir("RSA_Algorithm/");

				os.chdir("RSA_Encryption_Prime1/");

				os.chdir("RSA_Encryption_Prime2/");

				os.chdir("RSA_Public_Key_For_Encryption/");

				a=os.path.abspath("");

				sys.path.append(a);

				from rsa_public_key_for_encryption import E;

				E();

	except KeyboardInterrupt:

		clear();


		

		NAME();



		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Number for Public Key which is Greater Than 1 and Less Than {}\n".format(phie_n)+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_public_key_for_encryption import E;

		E();

	except EOFError:

		clear();


		

		NAME();



		rsa_name();

		encryption_name();

		print("\033[1;34;40m"+"First Prime : "+"\033[1;35;40m"+'"'+prime1+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Second Prime : "+"\033[1;35;40m"+'"'+prime2+'"\n'+"\033[0m"); 

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered a Number for Public Key which is Greater Than 1 and Less Than {}\n".format(phie_n)+"\033[0m");

		os.chdir("..");

		os.chdir("RSA_Algorithm/");

		os.chdir("RSA_Encryption_Prime1/");

		os.chdir("RSA_Encryption_Prime2/");

		os.chdir("RSA_Public_Key_For_Encryption/");

		a=os.path.abspath("");

		sys.path.append(a);

		from rsa_public_key_for_encryption import E;

		E();

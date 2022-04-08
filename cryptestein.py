if(__name__=="__main__"):
	import sys
	from os import system, name
	def clear(): 

		if name == 'nt': 
			_ = system('cls') 

		else: 
			_ = system('clear')




	clear();



	print("\033[1;34;40m"+"""\n________________________.___.________________________________ _______________________________.___ _______   \n\_   ___ \______   \__  |   |\______   \__    ___/\_   _____//   _____/\__    ___/\_   _____/|   |\      \  \n/    \  \/|       _//   |   | |     ___/ |    |    |    __)_ \_____  \   |    |    |    __)_ |   |/   |   \ \n\     \___|    |   \\"""+"""\____   | |    |     |    |    |        \/        \  |    |    |        \|   /    |    """+"\\"+"""\n \______  /____|_  // ______| |____|     |____|   /_______  /_______  /  |____|   /_______  /|___\____|__  /\n        \/       \/ \/                                    \/        \/                    \/             \/ \n\t\t\t\t\t\t\t\t\t\t\t\t\t"""+"\033[1;35;40m"+"ρσωєяє∂ ву "+"\033[1;34;40m"+"Ϛì×Ƒìղցմɾҽ\n"+"\033[0m");

def Cryptestein():

	import time

	import os;

	import sys

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);

	from clear_function import clear;

	from program_name import NAME;

	from additive_name import additive_name;

	from multiplicative_name import multiplicative_name;

	from autokey_name import autokey_name;
	
	from rsa_name import rsa_name;

	from affine_name import affine_name;

	from help_name import help_name;

	from exit_function import exit;

	try:
		
		cryptestein=input("\033[1;32;40m"+"【1】 Additive Cipher\n\n【2】 Multiplicative Cipher\n\n【3】 Autokey Cipher\n\n【4】 RSA Algorithm\n\n【5】 Affine Cipher\n\n【6】 Help\n\n【7】 Exit\n\n"+"\033[1;36;40m"+"Choose an Option : "+"\033[0m");
	
		if cryptestein=='1':

			clear();

			NAME();

			additive_name();	

			os.chdir("..");

			os.chdir("Additive_Cipher/");

			a=os.path.abspath("");

			sys.path.append(a)

			from additive_cipher import Crypt;

			Crypt();

		elif cryptestein=='2':

			clear();			

			NAME();

			multiplicative_name()	

			os.chdir("..");
			
			os.chdir("Multiplicative_Cipher/");
			
			a=os.path.abspath("");
			
			sys.path.append(a);
			
			from multiplicative_cipher import Cyber;

			Cyber();


		elif cryptestein=='3':


			

			clear();


			

			NAME();

			autokey_name()	

			os.chdir("..");
			
			os.chdir("Autokey_Cipher/");
			
			a=os.path.abspath("");
			
			sys.path.append(a);
			
			from autokey_cipher import Autokey;
			
			Autokey();

		elif cryptestein=='4':


			

			clear();


			

			NAME();

			rsa_name()	
			
			os.chdir("..");
			
			os.chdir("RSA_Algorithm/");
			
			a=os.path.abspath("");
			
			sys.path.append(a);
			
			from rsa_algorithm import RSA;
			
			RSA();

		elif cryptestein=='5':


			

			clear();


			

			NAME();

			affine_name()	
			
			os.chdir("..");
			
			os.chdir("Affine_Cipher/");
			
			a=os.path.abspath("");
			
			sys.path.append(a);
			
			from affine_cipher import Affine;
			
			Affine();

		elif cryptestein=="6":
			
			clear();

			NAME();

			help_name();

			os.chdir("..");
			
			os.chdir("Help/");
			
			a=os.path.abspath("");
			
			sys.path.append(a);
			
			from cryptestein_help import Help;			

			Help();
		elif cryptestein=="7":
			exit();

		elif cryptestein=="":

			


			
			clear();


			
				
			NAME();
				

			
				
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

			
			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein import Cryptestein;		

			Cryptestein();
			
		else:

			


			
			clear();


			
				
			NAME();
				

			
				
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered",'"'+cryptestein+'"'", you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");
			
			os.chdir("..");

			a=os.path.abspath("");

			sys.path.append(a);

			from cryptestein import Cryptestein;		



			Cryptestein();


	

	except KeyboardInterrupt:

		



		clear();


		
				
		NAME();


		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

		os.chdir("..");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein import Cryptestein;		
		
		Cryptestein();

	except EOFError:


			
		clear();


		
				
		NAME();


		

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'1'"' or '"'2'"' or '"'3'"' or '"'4'"' or '"'5'"' or '"'6'"'\n"+"\033[0m");

		os.chdir("..");

		a=os.path.abspath("");

		sys.path.append(a);

		from cryptestein import Cryptestein;		
		
		Cryptestein();

Cryptestein();

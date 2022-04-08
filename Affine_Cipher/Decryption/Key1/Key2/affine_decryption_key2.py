key2="";
decrypted_word="";

def K2(): 

	import os;

	import sys

	os.chdir("..");

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

	os.chdir("Key1/");
	
	a=os.path.abspath("");

	sys.path.append(a);

	from affine_decryption_key1 import key1;

	from affine_decryption_key1 import decrypt_val1;

	os.chdir("Key2/");

	os.chdir("User/");

	a=os.path.abspath("");

	sys.path.append(a);
	
	from affine_decryption_user_function import User;

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("..");

	os.chdir("Base/");

	a=os.path.abspath("");

	sys.path.append(a);
		
	try:

		global decrypted_word;

		global key2;

		key2=input("\033[1;32;40m"+"【A】 Back\n\n【B】 Exit\n\n"+"\033[1;36;40m"+"Enter the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters : "+"\033[0m");




		clear();




		NAME();


		affine_name();

		decryption_name();

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		if key2=="A":
			
			clear();


	

			NAME();

			affine_name();

			decryption_name();

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key1 import K1;

			print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

			K1();

		elif key2=="B":
			exit();	

		elif key2=="":

			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Entered Nothing and Pressed "'"Enter"'""+", you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			os.chdir("Key2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key2 import K2;

			K2();




		k=True;

		if key2.isdigit()!=True:
			k=False

		elif int(key2)>25:
			k=False

		elif int(key2)<0:
			k=False



		if k==False:
			print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You did not Follow the Instructions and Entered "+'"'+key2+'"'+" which contains unacceptable characters\n"+"\033[0m");

			os.chdir("..");

			os.chdir("Affine_Cipher/");

			os.chdir("Decryption/");

			os.chdir("Key1/");

			os.chdir("Key2/");

			a=os.path.abspath("");

			sys.path.append(a);

			from affine_decryption_key2 import K2;




			K2();
		


		
		else:

			print("\033[1;34;40m"+"Key2 : "+"\033[1;35;40m"+'"'+key2+'"\n'+"\033[0m");

			if int(key2)==0:
				gcd=26;
			
			if int(key2)>26:
				smaller=26;
			
			else:
				smaller=int(key2);
			for i in range(1,smaller+1):

				if((int(key2)%i==0)and(26%i==0)):
					gcd=i;
			if gcd==1:
				t1=0;
				t2=1;
				r2=int(key2); 
				r1=26

				while r2!=0:
					q=r1//r2;
					r=r1%r2;
					t=t1-(q*t2);
					r1=r2;
					r2=r;
					t1=t2;
					t2=t;
				if t1<0:
					t1=t1+26;

				decrypt_val2=[];
				start=0;
				for den_val in decrypt_val1:
					if den_val==32:
						decrypt_val2.append(32);
						start=start+1;
					else:				
						a=int(decrypt_val1[start])*int(t1);
						if a<0:
							a=a+26;
							m=a%26;
							decrypt_val2.append(m);
							start=start+1;
						else:
							m=a%26;
							decrypt_val2.append(m);
							start=start+1;
			
				decrypt_num=0;
				decrypt_word=[];
				for i in decrypt_val2:
					if i==32:
						decrypt_word.append(chr(32));
					else:				
						decrypt_num=97+i;
						decrypt_word.append(chr(decrypt_num));
						decrypt_num=0;
			
				decrypted_word="";
				for decrypt_letter in decrypt_word:
					decrypted_word=decrypted_word+decrypt_letter;

				print("\033[1;34;40m"+"Plain Text : "+"\033[1;35;40m"+'"'+decrypted_word+'"\n'+"\033[0m");
			
				User();

			else:
					
				print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"Multiplicative Inverse does not exists at key =",key2,"\n"+"\033[0m");

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

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key1/");

		os.chdir("Key2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_decryption_key2 import K2;

		K2();

	except EOFError:

		clear();


		

		NAME();



		affine_name();

		decryption_name();	

		print("\033[1;34;40m"+"Encrypted Text : "+"\033[1;35;40m"+'"'+inp+'"\n'+"\033[0m"); 

		print("\033[1;34;40m"+"Key1 : "+"\033[1;35;40m"+'"'+key1+'"\n'+"\033[0m");

		print("\033[1;33;40m"+"oosy : "+"\033[1;31;40m"+"You Interrupted the Working of the Program, you should have Entered Either '"'A'"' or '"'B'"' or should have Entered the Value of Key in Numeric Characters only and between 0 to 25 without Special Characters\n"+"\033[0m");

		os.chdir("..");

		os.chdir("Affine_Cipher/");

		os.chdir("Decryption/");

		os.chdir("Key1/");

		os.chdir("Key2/");

		a=os.path.abspath("");

		sys.path.append(a);

		from affine_decryption_key2 import K2;

		K2();

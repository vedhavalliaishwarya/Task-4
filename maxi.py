Tamil=int(input("Enter the Tamil Mark:"))
English=int(input("Enter the English Mark:"))
Maths=int(input("Enter the Maths Mark:"))
Physics=int(input("Enter the Physics Mark:"))
Computer=int(input("Enter the Computer Mark:"))
max=100;
if(Tamil>English and Tamil>Maths and Tamil>Physics and Tamil>Computer):
	print("Tamil Mark is Maximum one");
elif(English>Maths and English>Physics and English>Computer):
	print("English Mark is Maximum one");
elif(Maths>Physics and Maths>Computer):
	print(" Maths Mark is Maximum one");
elif(Physics>Computer):
	print("Physics Mark is Maximum one");
elif(Computer<max):
	print("Computer Marks is Maximum One");
else:
	print("No Maximum Mark found");
if(Tamil<English and Tamil<Maths and Tamil<Physics and Tamil<Computer):
	print("Tamil Mark is Minimum one");
elif(English<Maths and English<Physics and English<Computer):
	print("English Mark is Minimum one");
elif(Maths<Physics and Maths<Computer):
	print(" Maths Mark is Minimum one");
elif(Physics<Computer):
	print("Physics Mark is Minimum one");
elif(Computer<max):
	print("Computer Marks is Minimum One");
else:
	print("No Minimum Mark found");

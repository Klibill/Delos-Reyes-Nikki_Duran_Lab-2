#Laboratory_Activity_No_2_Emerging-Tech
# Author: Delos Reyes, Nikki
#	  Duran, Klibill

print("Computation of Student Average Grade Program")
print("")
print("Enter Student Grades")
Prelim = float(input("Prelims: "))
Midterm = float(input("Midterms: "))
Semifinal = float(input("Semifinals: "))
Final = float(input("Finals: "))

sum = Prelim + Midterm + Semifinal + Final
avg = sum/4

print ("Your Average is {}." .format(avg))
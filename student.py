rollno=int(input("Enter rollno value:"))
name=input("Enter Your name:")
fee=float(input("enter Your Fee amount:"))
sub1=int(input("Enter Sub1 marks:"))
sub2=int(input("Enter Sub2 marks:"))
sub3=int(input("Enter Sub3 marks:"))
print("Student Rollno:",rollno)
print("Student Name:",name)
print("Student Fee Amount=",fee)
print("SUB1=",sub1,"\tSUB2=",sub2,"\tSUB3=",sub3)
total=sub1+sub2+sub3
avg=total/3
print("Student Total Marks=",total)
print("Avearage Marks=",avg)
if avg>=80:
    print("A grade")
elif avg>=70 and avg<80:
    print("B grade")
elif avg>=60 and avg<70:
    print("C grade")
elif avg>=50 and avg<60:
    print("D grade")
else:
    print("Student is Fail")
print("Record End")



+++++++++++++++++++++++++++++++++

Enter rollno value:99
Enter Your name:Kavya
enter Your Fee amount:10000.987
Enter Sub1 marks:80
Enter Sub2 marks:56
Enter Sub3 marks:70
Student Rollno: 99
Student Name: Kavya
Student Fee Amount= 10000.987
SUB1= 80 	SUB2= 56 	SUB3= 70
Student Total Marks= 206
Avearage Marks= 68.66666666666667
C grade
Record End
>>> 

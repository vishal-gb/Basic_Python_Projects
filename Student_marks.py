name=input("Enter Student Name:")
Subject1=int(input("Enter Subject1 marks:"))
Subject2=int(input("Enter Subject2 marks:"))
Subject3=int(input("Enter Subject3 marks:"))
total=Subject1+Subject2+Subject3
average=total/3
print(total,"is the total marks")
print(average,"is the average marks")
if(Subject1>50):
    if(Subject2>50):
        if(Subject3>50):
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")
else:
    print("FAIL")

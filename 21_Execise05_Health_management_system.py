v1=open("varadWorkout.txt","r+")
v2=open("varadDiet.txt","r+")
p1=open("pranavWorkout.txt","r+")
p2=open("pranavDiet.txt","r+")
a1=open("abhiWorkout.txt","r+")
a2=open("abhiDiet.txt","r+")
print("Welcome to the Health Management System !!!!!")
print(" ")
no1=int(input("Enter the 0 or 1 to lock or retrive a data : \n"))
lock=0
retrive=1


def getdate():
    import datetime
    return datetime.datetime.now()


if(no1==lock):
    no2=int(input("Enter a client name :varad as 1 , pranav as 2 , abhi as 3 \n"))
    if(no2 == 1):
        no3=int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if(no3==0):
            print("Enter the workout plan")
            v1.write(input())
        else:
            print("Enter the Diet plan")
            v2.write(input())
    if (no2 == 2):
        no4 = int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if (no4 == 0):
            print("Enter the workout plan")
            p1.write(input())
        else:
            print("Enter the Diet plan")
            p2.write(input())
    if (no2 == 3):
        no5 = int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if (no5 == 0):
            print("Enter the workout plan")
            a1.write(input())
        else:
            print("Enter the Diet plan")
            a2.write(input())
elif(no1==retrive):
    clname=int(input("Enter a client name :varad as 1 , pranav as 2 , abhi as 3 \n"))
    if (clname == 1):
        wd = int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if (wd == 0):
            print(v1.readline())
            print(getdate())
        else:
            print(v2.readline())
            print(getdate())
    if (clname == 2):
        wd = int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if (wd == 0):

            print(p1.readline())
            print(getdate())
        else:
            print(p2.readline())
            print(getdate())

    if (clname == 3):
        wd = int(input("enter the workout or Diet : workout as 0 Diet as 1: \n"))
        if (wd == 0):
            print(a1.readline())
            print(getdate())
        else:
            print(a2.readline())
            print(getdate())
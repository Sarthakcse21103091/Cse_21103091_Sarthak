#QUESTION 1

#Python Program to Count Occurrence of a Character in a String

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The total Number of Times ", char, " has Occurred = " , count)


print(100*("-x"))

#QUESTION 2

print("Question 2")
while(True):#while loop is used so that if any wrong value is entered then will be entered again
    day=int(input("ENTER THE DAY:"))
    if(1<=day<=31):
        break
    else:
        print("Enter a valid date")

while(True):
    month=int(input("Enter the month:"))
    if(1<=month<=12):
        break
    else:
        print("Enter a valid month")

while(True):
    year=int(input("Enter a year between 1800 and 2025:"))
    if(1800<=year<=2025):
        break
    else:
        print("Enter the year between 1800 and 2025 only")
if(month==1 or 3 or 5 or 7 or 8 or 10):
    if(day==31):
        day=1
        month=month+1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")

elif(month==4 or 6 or 9 or 11):
    if(day==30):
        day=1
        month=month+1
        print(day,"/",month,"/",year)
    elif(day<30):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")

elif(month==2):
    if((year%400==0) or
    (year%100 !=0) and
    (year%4 == 0) ):
      if(day==29):
          day=1
          month=month+1
          print(day,"/",month,"/",year)
      elif(day<29):
          day+=1
          print(day,"/",month,"/",year)
      else:
          print("please enter correct date")

    else:
        if(day==28):
            day=1
            month+=1
            print(day,"/",month,"/",year)
        elif(day<28):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("please enter correct date")

elif(month==12):
    if(day==31):
        day=1
        month=1
        year+=1
        print(day,"/",month,"/",year)
    elif(day<31):
        day+=1
        print(day,"/",month,"/",year)
    else:
        print("please enter correct date")
else:
    print("9please enter correct date")



print(100*("-x"))


#QUESTION 3

my_list = [3,9,10]
print('The list is')
print(my_list)
print('The resultant tuple is :')
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)

print(100*("-x"))


# QUESTION 4

#firstly take input of grade from the user...
print('enter grade of student:')
n1=int(input())

if n1==10:
    print("your grade is 'A+' and outstanding performance")
elif n1==9:
    print("your grade is 'A' and excellent performance")
elif n1==8:
     print("your grade is 'B+' and very good performance")
elif n1==7:
     print("your grade is 'B' and good performance")
elif n1==6:
     print("your grade is 'C+' and average performance")
elif n1==5:
     print("your grade is 'C' and below average performance")
elif n1==4:
     print("your grade is 'D' and poor performance")
else:
    print('error')

print(100*("-x"))


#QUESTION 5

i=0
a="ABCDEFGHIJK"
for i in range(6):
    j=i
    while (j>0):
        print(" ",end="")
        j=j-1
    k=0
    for k in range (len(a)-2*i):
        print(a[k],end="")
        
    print("")
   
  
# QUESTION 6

sid=int(input("Enter your sid: \n"))
name=input("Enter name: \n")
students={sid:name}

while True:
    option=input("Do you want to enter another student entry(Y or N):").upper()
    if option=='Y':
        sid=int(input("Enter sid: "))
        name=input("Enter name: ")
        students[sid]=name
    elif option=='N':
        break
    else:
        print("Invalid input!")

# part(a)-print the dictionary
print("<a>\n",students)

#part (b)-sort according to the names
print("<b>\n",{k:v for k,v in sorted(students.items(), key=lambda x:x[1])})

#part (c)-sort according to the sids 
print("<c>\n",{k:v for k,v in sorted(students.items())})

#part (d)-search for a student by their sid 
sid=int(input("Search Name with SID: \n"))
print("<d>\n",students[sid])

print(100*("-x"))


# QUESTION 7
    
# Function to display the Fibonacci sequence
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES:  \n"))
if no_of_terms <=0:
    print("Please enter positive integer")
else:
    print("Fibonacci sequenceL: ")
    sum=0
    for i in range(no_of_terms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AVERAGE OF THE RESULTANT FIBONACCI SERIES IS: ",avg)

print(100*("-x"))


# QUESTION 8

Set_1 ={1,2,3,4,5}
Set_2 ={2,4,6,8}
Set_3 ={1,5,9,13,17}

#part (a)
Set_union=Set_1.union(Set_2)
Set_intersection=Set_1.intersection(Set_2)
Part_A_Set=Set_union - Set_intersection
print("<a>\n",Part_A_Set)

#part (b)-eliminating intersection of sets taken two at a time from the union of all three sets 
Part_B_set= Set_1.union(Set_2.union(Set_3))- Set_1.intersection(Set_2) -Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print("<b>\n",Part_B_set)

# part (c)-subtracting intersection of three from two taken at one time
Part_C_Set=((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3))))-(Set_1.intersection(Set_2.intersection(Set_3)))
print("<c>\n",Part_C_Set)

#part (d)- ignoring the numbers from 1 to 10 that are occuring in set1
Part_D_Set=set()
for i in range(1,11):
    if i not in Set_1:
        Part_D_Set.add(i)
print("<d> \n",Part_D_Set)

#part e
Part_E_Set=set()
if i in range(1,11):
    if i not in Set_1 and i not in Set_2 and i not in Set_3:
        Part_E_Set.add(i)
print("<e>\n",Part_E_Set)

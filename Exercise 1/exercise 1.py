cookie = "alien"
x =  2.5
y = -1.5
m =  18
n =  4

from math import sqrt

### Oppgave 1 ###
print("Oppgave 1")
print(x+n*y-y*(x+n))
print(m//n+m%n)
print(1-(1-(1-(1-(1-n)))))
print(sqrt(sqrt(n)),"\n")

### Oppgave 2 ###
print("Oppgave 2")

n = 17

print(n//10+n%10)
print(n%2+m%2)
print((m+n)//2)
print((m+n)/2)
print(int(round(0.5*(m+n))),"\n")

### Oppgave 3 ###
print("Oppgave 3")

s = "Hello"
t = "World"

print(len(s)+len(t))
print(s[1]+s[2])
print(s[len(s)//2])
print(s+t)
print(t+s)
print(s*2,"\n")

### Oppgave 4 ###
print("Oppgave 4","\n")

print("Shit-o-lator","\n",)
print("a = Sum")
print("b = Difference")
print("c = Product")
print("d = Average")
print("e = Distance")
print("f = Maximum")
print("g = Minimum")
print("Spacebar to skip")

calc = input("What will it be, friend? ")

if calc == "a" :
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print(int_1 + int_2)

    
elif calc == "b":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print(int_1/int_2)
    
    
elif calc == "c":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print(int_1*int_2)
    
    
elif calc == "d":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print((int_1+int_2)/2)
    
    
elif calc == "e":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    #print("%.1f" % sqrt(int_1**2+int_2**2))
    #print(max(int_1,int_2)-min(int_1,int_2))
    print(abs(int_1 - int_2))
    

elif calc == "f":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print(max(int_1,int_2))
    
    
elif calc == "g":
    int_1 = int(input("Enter a number: "))
    int_2 = int(input("Enter another number: "))
    print(min(int_1,int_2))
    
    
else:
    print("Skipped","\n")

### Oppgave  ###
##  Input 20 and 25 in Oppgave 4

### Oppgave 6 ###
print("Oppgave 6","\n")

print("Input Lengths of the side of the rectangle")
A = int(input("Width: "))
B = int(input("Height: "))

print(f"with the length sides of {A} and {B} you get:","\n")

print("Area= ",A+B)
print("Perimeter= ",2*(A+B),"\n")

### Oppgave 7 ###
print("Oppgave 7","\n")

Q = input("Write a word: ")
W = len(Q)

if Q.isalpha():
    if W <= 3:
        print("Input must equal to or more than 4 characters")
    else:
        print(Q[0] + Q[1] + "..." + Q[len(Q)-2] + Q[len(Q)-1],"\n")
else:
    print("You must type letters!")

å = input("Input a five-digit number: ")

if å.isdigit(): 
    if len(å) == 5:
        print(å[0],å[1],å[2],å[3],å[4])
    else :
        print("Not a five-digit number :-(")
else:
    print("You must input digits!")
    
    
### Tull
alien = input("Password: ")
if alien == cookie:
    print("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒")
    print("▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒")
    print("▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒")
    print("▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒")
    print("▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒")
else:
    print("Wrong password")
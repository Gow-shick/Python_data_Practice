
#Multiple assignment
x,y,z=1,2,3

print(z)  

#concate string and int not possible still if we convert the int to string as below

c="Ram"
d="10"
print(c+d)

#type casting explicit and implicit

a=5
b=5.6

k=a+b

print(k) 
print(type(k)) #implicit type casting indirectly it converting to float 

print(type(d)) #give data type of the d

print(a+int(d)) #explicit type casting converting the d into integer.

#comment # is the single line comment for explaining a code

"""
Tirpple Quote is the 
multiline comment for very long comments

"""


#Multimline code doing by '\' like below

total_sum=12+20+30+45+\
70+90

print(total_sum)


#indentation is used below to structure the body of if else code there will be 4 space default before print.

if a>10:
    print("'a' value is more than 10")   
else:
    print("'a'value is not more than 10")
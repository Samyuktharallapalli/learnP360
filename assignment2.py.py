# question 1
x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5 + 5j], 4000]

print(x[4][0], x[4][1], x[4][6], x[4][4][2], x[4][4][3])

print(x[3], x[4][4], x[4][5])

# question 2

sum1=0
sum2=0
for i in range(1,22):
    if i%2==0:
        sum1+=i
        i+=1
        for j in range (i+1,22):
            if j%2==0:
                sum2+=j
                j+=1
                print(i,j)

# Question 3
x=input("enter a string")
thisdict = {"@":1, "#":3, "$":4, "%":5, "^":6, "&":7, "*":8, "!":9, "~":10}
count=0
for i in x:
    if i in count.keys:
		count[i] += 1
		print(count)

# question4
list1=0
for i in range(1,51):
    list1 = i**3
    i=i+1
    if i%2 == 0 in range(1,51):
        if i**3<51:
            print("the cube numbers are:")
            print(list1)
	
# question5

list2=[1,2,3,4,5]
x= list2.copy()
print(x)
temp=[]
for i in x:
    temp=i*3
    i=i+1
    print(temp)

# question6

str = ["Hello world I am learning python"]
print(str)
a=str.split(' ')
print(a)
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))
print(len(a[3]))
print(len(a[4]))
print(len(a[5]))

# question 7

mylist1 = input("enter something")

if mylist1 is int():
    print("true")
else:
    print("false")
	

   
	


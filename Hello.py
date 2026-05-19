print ("Python is working")

if 5 > 4:
    print("i am a good boy")

x = 5
y = "John"

print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "pinapple", "orange"]
a, b, c = fruits
print(c)

x = "Python"
y = "is"
z = "awesome"
print (x, y, z)


p = q = r = "Hello Blessed trust you are good"
print(q)

x = 83
y = "Alfred"
print(x,y)

x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()

Joe = """hello joe how are tou doe id aien aidlei aiefjei aeijf i aefieii adfdsfj iosdf 
 dsfj fdsfij aij ohow are you doing i hope you are doing wellfajo
 a jfldsk aldk ej dfjdkllejadf"""
print(Joe)
print(len(Joe))

b = "Second Semester"
print(b[0])
print(b[9])
print(b[7:12])
print(b[:8])
print(b[4:])
print(b.upper())
print(b.lower())

fee = 5000
txt = f"The fee is {fee} naira"
print(txt.format(fee))
print(txt)
print("The fee is " + str(fee) + " naira")


x = 15
y = 4

print(x//y)

thislist = ["apple", "22", "orange","9", "cherry", "53", "19", "mango", "93", "pawpaw","30", "banana"]
print(thislist)
print(thislist[1])
print(thislist[2:5])
print(thislist[:4])
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = tuple3 * 4
print(tuple4)


# SET
thisset = {"apple", "banana", "cherry"}
theset = {"pineapple", "mango", "papaya"}
for x in thisset:
  print(x)
print("banana" in thisset)
thisset.add("Guava")
print(thisset)
thisset.update(theset)
print(thisset)


set1 = {"a", "b" , "c", "d", "e"}
set2 = {"d", "e", "f", "g", "h"}
set3 = set1.union(set2)
print(set3)
set4 = set1 | set2
print(set4)
set5 = set1.intersection(set2)
print(set5)
set6 = set1.difference(set2)
print(set6)
set7 = set1.symmetric_difference(set2)
print(set7)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
thisdict["year"] = 2018
print(thisdict)




# thislist = ["banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


#   thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# list = ["ple", "ana", "erry"]
# for i in range(len(list)):
#   print(list[i])

# this = ["apple", "banana", "cherry"]
# i = 1
# while i < len(this):
#   print(this[i])
#   i = i + 1


#PYTHON IF STATEMENT
age = 50
if age >= 20:
  print("You are old")
  print("call me daddy")

a = 33
b = 33
if b > a:
  print("b is greater than a")  
elif a == b:
  print("a and b are equal")

username = "Tobias"
password = "12345"
is_verified = False

if username and password and is_verified:
    print("Login successful")
else:
   print("Login failed")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


# WHILE LOOP
i = 29
while i > 25:
  print(i)
  i = i - 1


# FUNCTIONS

def my_function():
  print("Hello, just started off with functions")
my_function()
my_function()

def do_function():
  return "Why are you not in the party"
print(do_function())

def d_function(name):
  print("Hello " + name)
d_function("Tobias")
d_function("Alfred")
d_function("Gideon")

def my_function(animal, name):
  print("i hav a", animal)
  print("my", animal + "'s name is", name)
my_function(animal = "dog", name = "Browndy")
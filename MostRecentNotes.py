import random


def funPause1():
	while True:
		intAnswer_Temp = input("Exit (y/n): ")
		if intAnswer_Temp == "y": 
			print("\n"*4)
			exec(open("get.py").read())
			break


str1 = "avbcd_12530! xyZ"
str2 = "baU*8"
print(str1.title())
#Avbcd_12530! Xyz | captializes the first letter

print(str1.upper())
#AVBCD_12530! XYZ
print(str2.lower())
#bau*8



print(f"{str1} {str2.upper()}")
#avbcd_12530! xyZ BAU*8

print("{}, and {}!".format(str2,str1))
#baU*8, and avbcd_12530! xyZ!


# python special characters:
# \n new line, \t tab, \r Carriage return (jumps to the start of the line), \b backspace \f Form feed
# \\ backslash, \', \", 
#\v vertical tab (new line then pushes the content of the next value at the same distance vertically), adjusts to the command line length

str3 = str(random.randint(0,90000000000))*10
print(str1 + "\v" + str2 + "\v\n" + str2 + "\v"+str3+"\v" + str1)
#avbcd_12530! xyZ
#                baU*8
#
#baU*8
#     19714035660197140356601971403566019714035660197140356601971403566019714035660197140356601971403566019714035660
#(same line but wrapped in the command line)
#178560344741785603447
#                     avbcd_12530! xyZ



print(str1 + "\r" + str2)
#baU*8_12530! xyZ

print("\110\n"+"\xf2\n"+"\54\a")
#H	Ascii # to char
#ò	Hex to ASCII char
#l	same as H output

str3 = str1+" "
print((str3).rstrip()+"."+str2)
#avbcd_12530! xyZ.baU*8
#Removes the trailing space from the line example "xy z " to "xy z"
#.strip() removes from left and right
#.lstrip() (strips it from the left of the string

#can avoid errors in script if using ' in it by encling it in " ' " or vice versa ' " ' 

# +, -, /, *, % modulus, ** exponent, // floor division 9//2=4
#x//=a is the same as x=x//a

#Assignment operators: ==, !=, <>, <, >, >=, <=

#Bitwise operators: & and, | or, ^ xor, ~ flips bits, <<< binary leftshift, <<< rightshift
#Used for binary math

#Logical operators: and, or, not( x and y)

#Multiple assessments we want int3 to be a constant (doesn't actually make it a constant, just a visualizationed organization
int1,int2,INT3 = 1_000,1230,5_994_002
print(int1,int2,INT3)
#1000 1230 5994002


strTestArr = []
strTestArr = ["Abcd","efg","lMno","pQrsT"]
print(strTestArr[2].title())
#Lmno
print(strTestArr[-1])
#pQrsT
print(f"First 4 letters of alphabet: {strTestArr[0].lower()} < < = =")
#First 4 letters of alphabet: abcd < < = =


strTestArr.append("xyZ")

#Pushes variable to the right if value is 0 or positive, if negative inserts it from the right to the left pushing the variable still to the right surprisingly
strTestArr.insert(1,"!:!:!")
print(strTestArr)
#['Abcd', '!:!:!', 'efg', 'lMno', 'pQrsT', 'xyZ']

strTestArr.insert(-1,"AAAAAAAs")
print(strTestArr)
#['Abcd', '!:!:!', 'efg', 'lMno', 'pQrsT', 'AAAAAAAs', 'xyZ']


del strTestArr[1] # removes item at the position 1
print(strTestArr)
#['Abcd', 'efg', 'lMno', 'pQrsT', 'AAAAAAAs', 'xyZ']

print(strTestArr.pop(1)) #actually states what item was removed, output: efg
print(strTestArr)
#['Abcd', 'lMno', 'pQrsT', 'AAAAAAAs', 'xyZ']

strTestArr.append("pQrsT")
strTestArr.remove("pQrsT")
print(strTestArr) # removes the first encounter
#['Abcd', 'lMno', 'AAAAAAAs', 'xyZ', 'pQrsT']



strTestArr.sort() #Put the following argument in the parenthesis to reverse the string: reverse=True 
print(strTestArr) # ['AAAAAAAs', 'Abcd', 'lMno', 'pQrsT', 'xyZ']


print(len(strTestArr)) #Elements in the row: 5

print(len(strTestArr[0])) #Characters in a string 8


print(strTestArr[::-1]) #Reverses the array without changing the value of an array (does not work for a string)
#['xyZ', 'pQrsT', 'lMno', 'Abcd', 'AAAAAAAs']


for itemFromArray in strTestArr:
	print(itemFromArray)		#outputs the array 1 item per line



for intCounter1 in range(0,10): print(intCounter1)
# prints from 0 to 9 does not print 10!!!

intNumberArr=list(range(0,13,4)) #converts the range into a list. 
#start at 0 end at 12 +1 (because last number is not printed, if not the list would be 0 4 8)
print(intNumberArr)
#[0, 4, 8, 12]

print(min(intNumberArr)) #0
print(max(intNumberArr)) #12
print(sum(intNumberArr)) #24

intListArr = [intCounter1**2 for intCounter1 in range(1,10)]
print(intListArr) # [1, 4, 9, 16, 25, 36, 49, 64, 81]



print(intListArr[3:7]) #excludes the 7th position
#[16, 25, 36, 49]

print(intListArr[:2])
#[1, 4]


print(intListArr[2:]) #(for functions also work with this)
#[[9, 16, 25, 36, 49, 64, 81]


intListArr[3]=0 #change a specific part of an array



#pep8 code formatting:
#strSampleArr = [0,8,
#		1,3,4,
#		6,2,9]

#make sure to add comments
# same thing for large summations or functions
# intLargeNumber = (int1 + int11 - int2
#		int3)



if "value1" == "value2": print("X")
elif "value2" == str(3): print("z")
else:
	print("xzyby")

bol1 = True
bol2 = False

#Creating a dictionary:
strValuesDict = {
		"color":"red", 
		"meme":["wojak", "wojack"], 
		"year":2022
		}
print(strValuesDict["meme"])
#wojak



strValuesDict["funny"] = "yes"
strValuesDict["rating"] = "70"

#strValuesDict["year"]++1 (doesn't work for dictionary)
strValuesDict["year"] = strValuesDict["year"] + 1
print(strValuesDict["year"])


#prints out the keys of the dictionary (both rows below do the same)
for dictKeys in strValuesDict: print(dictKeys)
for dictKeys in strValuesDict.keys(): print(dictKeys)

#prints out the value
for dictValues in strValuesDict.values(): print(dictValues)
#red
#['wojak', 'wojack']
#2023
#yes
#70













#dictionaries can be put into an array
strValuesDict1 = {
		"color":"red", 
		"meme":["wojak", "wojack"], 
		"year":2014
		}

strValuesDict2 = {
		"color":"yellow", 
		"meme":["doge", "doggo"], 
		"year":2015
		}

strValuesDict3 = {
		"color":"blue", 
		"meme":["quandale", "quandale dingle"], 
		"year":2022
		}
		
strValuesDict3 = {
		"color":"grey", 
		"meme":["cryptobro", "diamond hands", "NFTurd"], 
		"year":2021
		}

strDictionariesArr = [strValuesDict1,strValuesDict2,strValuesDict3]
print(strDictionariesArr)

for ValuesDict in strDictionariesArr[:2]:	#Parse only the first 2 values (0,1)
	if ValuesDict["color"] == "yellow":
		ValuesDict["year"] = 2014


#Can have dictionaries in dictionaries & lists within dictionaries. And vice versa.
strDictionariesArr = {
			"Key1":{
				"subKey1":1,
				"subKey2":"xyz"
				},
			"Key2":{
				"subKey23":4,
				"subkey5":209
				}
			}


for dctKey1, dctSubkey1 in strDictionariesArr.items():
	print(dctKey1)
	print(dctSubkey1)







#user input
print("Example")
#prints on a new line
#strUserInput = input(":")



while True:

	#break out of the script
	break
	



strSampleArr = ['xyZ', "Abcd", 'pQrsT', 'lMno', 'Abcd', 'AAAAAAAs']


print(strSampleArr)


while "Abcd" in strSampleArr:
	strSampleArr.remove("Abcd")

print(strSampleArr)









def funTester(strPassed='z'):
#default value is z, if no value is passed z is assumed to be the value
	print(f"Test has been executed: {strPassed} is the passed string.")
	if strPassed == "n": return "lmao"
	elif strPassed == "z": return "xD"
	else: pass #do nothing 




funTester("z")

funTester("n")


funTester("")

#if there are 2 values and one of them needs to be blank, define what value you're referring to
print(funTester(strPassed=""))
#Test has been executed:  is the passed string.
#None

print(funTester())
#Test has been executed: z is the passed string.
#xD







def funTester(strPassed='z'):
#default value is z, if no value is passed z is assumed to be the value
	print(f"Test has been executed: {strPassed} is the passed string.")
	if strPassed == "n": return "lmao"
	elif strPassed == "z": return "xD"
	else: pass #do nothing 














#strEtcInput accepts all other inputs, can be leveratged as strEtcInput as a list, ex with a forloop
def funTester2(strPassed='z', *strEtcInput):
#default value is z, if no value is passed z is assumed to be the value
	print(f"Test has been executed: {strPassed} is the passed string.")
	if strPassed == "n": return "lmao"
	elif strPassed == "z": return "xD"
	else: pass #do nothing 

funTester2("xd", 4, 5 ,"jajaja", 'n')


#** is referred to as **kwags
#strEtcInput accepts all other inputs, including keywords
def funTester3(strPassed='z', **strEtcInput):
#default value is z, if no value is passed z is assumed to be the value
	print(f"Test has been executed: {strPassed} is the passed string.")
	if strPassed == "n": return "lmao"
	elif strPassed == "z": return "xD"
	else: print(strEtcInput)

funTester3("xd", strFunny="lmaooo", strBigBrain="yes")
{'strFunny': 'lmaooo', 'strBigBrain': 'yes'}







#importing modules
#from module_name import function_name
#from module_name import as modN (this creates an alias for the module so you don't have to refer to it each time as a module_name)
#from module_name import function_name as modNaFuncName
#from module_name import * (imports everything from that module)
#from module_name import function_name1, function_name2
#if you save a file as module_name.py then import it via functions above, you can use its functions:
#module_name.function_name()









class Food:
	
	#instance that runs first when a class is created 
	#NEEDS TO BE __init__ and NEEDS to have self as first value!!!
	def __init__(self, name, calories):
		#Defines the input variables for this function
		self.name = name
		self.calories = calories
		#though this variable has not been passed, 
		#it declaires it as a local var for this class (it will not reset with every call)
		self.totalCalories = 0
		
	def funEat(self):
		
		self.totalCalories += self.calories
		print(f" You have eaten {self.name} which is {self.calories}")
		return self.calories
	#requires user input 
	def funExtraCalories(self, strUserInput):
		self.totalCalories += int(strUserInput)
		print(f"Additional calories added: {self.totalCalories}.")
		return self.totalCalories

	class worthit:
		#Imports variables from the other function if needed, the ones already there
		#methods are overwritten from the previous class so can reuse names 
		def __init__(self, name, calories, quality):
			#super().__int__ is necessary to refer to the other class correctly
			super().__init__(self, name, calories)
			
		#Function inside of internal class 
		def funIsItCheese(name):
			if str(name) == "cheese": return True
			else: return False
	#to call a function that is unique to the class inside of the class use self.funFunction


objPizzaSlice = Food("Pizza Slice", 600)

# cannot just add a variable to initiate a variable. Needs to be first declaired
intTotalCalories = 0
intTotalCalories += objPizzaSlice.funEat()

intTotalCalories += objPizzaSlice.funEat()

intTotalCalories += objPizzaSlice.funEat()

print(intTotalCalories)

#Returns the name in the class NOTICE IT DOES NOT HAVE PARENTHESIS IN THE END!!!
print(objPizzaSlice.name)
print(objPizzaSlice.funExtraCalories(1_990))


#
print(objPizzaSlice.worthit.funIsItCheese("cheese"))

#to import classes from file Fileroo.py type: From fileroo import Class,class2
#to import an entire module: import fileroo 
#to import all classes: from fileroo import *
#to import a class with an alias: from fileroo import class1 as cl1
#Classes should be in CamelCase - as a politeness




with open("list", "w") as file_object: 
	for intCounter in range(1,6):
		file_object.write(f"{str(random.randint(0,90000000000))}\n")


#Read file (if no path, it assumes it is local):
with open("list") as file_object:
	strContents = file_object.read()
print(strContents)


with open("list") as file_object:
	for strLine in file_object:
		#search operators: 	
		if "zo" in "zoology": print("lmao")
		if strLine.find("34") == -1: print(strLine)
		try:
			#returns position of first occurance
			strLine.index("s")
			
		except ValueError:
			print("no s :(")
		#else is applicable to tries
		else: print("S!")



#r is used to read (default), w overwrites the current content, a append to add content 
#utf-8 is unnecessary ,but can be useful if reading a file output that was explicitly generated by X
with open("list1", mode="w", encoding="utf-8") as file_object: 
	file_object.write(f"{str(random.randint(0,90000000000))}\n")
	file_object.write(f"{str(random.randint(0,90000000000))}")




intX = 0
try:
	intX = (5/0) #if you know what error will pop up you can explicitly declaire it,
	#if you do not know what error will pop up just leave it as except:
except ZeroDivisionError: print ("y u dividng by 0")
else:print(intX)






#convert string to list with a splitter (default is space if left with no parameter)

strSample1 = "cranky dog, silly cat"

print(strSample1.split())
#['cranky', 'dog,', 'silly', 'cat']

print("cranky dog, silly cat".split("a"))
#['cr', 'nky dog, silly c', 't']

print("cranky dog, silly cat".split(", "))
#['cranky dog', 'silly cat']

#This did not work, it requires to be broken up into several lines
#for strItems in strSample.split("a"): if "a" in strItems: print(strItems)

for strItems in strSample1.split(", "): 
	if "o" in strItems: print(strItems)



strSample1 = "Cranky dog, silly cat"
print(strSample1.count("c"))
#can put another () after a ()
print(strSample1.lower().count("c"))






strNumber1 = str(random.randint(0,9_000_000_000_000))
strNumber1Arr = strNumber1.split("0")

import json

strFilename = "numbers.json"
with open(strFilename, "w") as objFile:
	#obj file is necessary for dump function
	json.dump(strNumber1Arr, objFile)
with open(strFilename) as objFile:
	print(json.load(objFile))




#To conduct tests on existing code, read more documentation. Usually used to test prewritten code
#import unittest
#class TestStringMethods(unittest.TestCase):

#	def test_upper(self):
#		self.assertEqual('foo'.upper(),'FOO')
#		self.assertTrue('foo'.upper(),'FOO')
#		self.assertFalse('foo'.upper(),'FOO')
#		with self.assertRaises(TypeError):
#			print("error!!!")

#	def test_upp(self):
#		self.assertFalse('foo'.upper(),'FOO')
#		#if exception X is raised do the print
#		with self.assertRaises(TypeError):
#			print("error!!!")

#To actually run the test:
#if __name__ == '__main__':
#	unittest.main()


#======================================================================
#FAIL: test_upp (__main__.TestStringMethods)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "/home/popos/Documents/Relearning Python/get.py", line 592, in test_upp
#    self.assertFalse('foo'.upper(),'FOO')
#AssertionError: 'FOO' is not false : FOO
#
#======================================================================
#FAIL: test_upper (__main__.TestStringMethods)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "/home/popos/Documents/Relearning Python/get.py", line 588, in test_upper
#    self.assertFalse('foo'.upper(),'FOO')
#AssertionError: 'FOO' is not false : FOO
#
#----------------------------------------------------------------------
#Ran 2 tests in 0.001s
#
#FAILED (failures=2)
#======================================================================
#FAIL: test_upp (__main__.TestStringMethods)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "/home/popos/Documents/Relearning Python/get.py", line 592, in test_upp
#    self.assertFalse('foo'.upper(),'FOO')
#AssertionError: 'FOO' is not false : FOO
#
#======================================================================
#FAIL: test_upper (__main__.TestStringMethods)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "/home/popos/Documents/Relearning Python/get.py", line 588, in test_upper
#    self.assertFalse('foo'.upper(),'FOO')
#AssertionError: 'FOO' is not false : FOO
#
#----------------------------------------------------------------------
#Ran 2 tests in 0.001s
#
#FAILED (failures=2)



#lambda = small function with only 1 expression
#lambda ARGUMENTS : EXPRESSION
#Arguments are expected to pass values (intValue1, intValue2)
#Expression is the function that it does

lamAddTen = lambda intA : intA+10
print(lamAddTen(40))
#50

lamAdd2Values = lambda intA,intB : intA+intB
print(lamAdd2Values(20,5))
#25


#iterations 
arrList = (4,20,199,"end")
itrList = iter(arrList)

next(itrList)
print(next(itrList))
print(next(itrList))
print(next(itrList))

try:
	print(next(itrList))
except: print("Error too many iterations outside of boundaries")



















































import tr00bleshutr as ts1

ts1.funPause()













































funPause1()

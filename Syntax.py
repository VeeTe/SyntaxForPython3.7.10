import random


def funPause():
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












funPause()

#input: filename or /foulder/path/filename.py of the file form itself
#Logic: If answered yes (y) it reruns the program, if answered no (n) it continues with the program
def funPauseRerun(strProjectName):
	while True:
		intAnswer_Temp = input("\n\n[tr00bleshutr]\vExit (y/n): ")
		if intAnswer_Temp == "y": 
			print("\n"*10)
			exec(open(strProjectName).read())
		elif intAnswer_Temp == "n": break

#simple pause in code		
def funPause():
	intAnswer_Temp = input("\n\n[tr00bleshutr]\vPres [ENTER] to continue...\n\n")


#check the variable 
def funVariableCheck(strVariable):
	print(f"\n\n[tr00bleshutr]\vThe variable type is: {type(strVariable)}\nThe variable itself is: ({strVariable})\n\n")
	return type(strVariable)


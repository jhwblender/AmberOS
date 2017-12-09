#Jesse Wood
#White Blaze Architecture Compilation
#11/29/17

# --------------------- READING AND ORGINIZING FILES ---------------------
gate = []
in1 = []
in2 = []
gateNum = []

basicGates = ['and','or','xor','xnor','not','nand']

def printAll():
    longest = 0
    num = len(gate)
    for i in gate:
        if(len(i)>longest):
            longest = len(i)
    for i in range(num):
        print((longest-len(str(gateNum[i])))*' '+str(gateNum[i])+', ',end='') #line number
    print()
    for i in range(num):
        print((longest-len(gate[i]))*' '+gate[i]+', ',end='') #Gate type
    print()
    for i in range(num):
        print((longest-len(str(in1[i])))*' '+str(in1[i])+', ',end='')  #in 1  
    print()
    for i in range(num):
        print((longest-len(str(in2[i])))*' '+str(in2[i])+', ',end='') #in 2
    print("\n")

def compileModule(fileName, currentNum, inGates, pastNum): #Recursive function
    print("Incoming Gates: ", end = "")
    print(inGates)
    
    outGates = []
    numInputs = 0
    
    def readLine():
                return myFile.readline()[:-1]

    def readNum():
        try:
                return int(myFile.readline()[:-1])
        except:
            print("Problem child: "+myFile.readline())

    print("Opening "+fileName)
    myFile = open(fileName,'r')
    while 1:                                    #Looping through module file
        line = myFile.readline()[:-1]
        print ("line: "+line)
        if(line in basicGates):                 #Basic Gates
            gate.append(line)
            first = readNum()
            second = readNum()
            if(first>numInputs):              #Something's broken here
                in1.append(first+currentNum)
            else:
                in1.append(inGates[first])
            if(second>numInputs):
                in2.append(second+currentNum)
            else:
                in2.append(inGates[second])
            
        elif(line == 'inputs'):                 #Inputs
            if(fileName=="system.txt"):
                numInputs = readNum()
                if(numInputs != len(inGates)):
                    print("ERROR: inputs/outputs mismatch")
                for i in range(numInputs):
                    gate.append("input")
                    in1.append(0)
                    in2.append(0)
            else:
                currentNum-=readNum()
                
        elif(line == 'outputs'):                #Output
            if(fileName=="system.txt"):
                for i in range(readNum()):
                    gate.append("output")
                    in1.append(readNum())
                    in2.append(0)
            else:
                for i in range(readNum()):
                    outGates.append(readNum())
                
        elif(line == '' or line == 'end'):      #End of module
            break
        
        else:                                   #Custom Module (recursion happens here)
            outGates = []
            for i in range(readNum()):
                outGates.append(readNum())
            currentNum = compileModule(line+'.txt', len(gate), outGates, currentNum)
            
        
    print("Closing "+fileName)
    myFile.close()
    return len(basicGates)-2 #Why -2.... idk, but so far it's working

#fileName = input("full file name: ")
fileName = "system.txt"
compileModule(fileName, 0, [], 0)

for i in range(len(gate)):
    gateNum.append(i)

printAll()
#print(out)

#------------------------------- CLEANING ARRAYS -------------------------
#this is mostly to get rid of all the extra outputs as well as make the gates ints from strings
"""
#finding output gates to delete
toDelete = []
for i in gateNum:
    if(gate[in1[i]] == 'output' and in1[i] not in toDelete):
        toDelete.append(in1[i])
    if(gate[in2[i]] == 'output' and in2[i] not in toDelete):
        toDelete.append(in2[i])
toDelete.sort(reverse = True)

#Re-connecting inputs to shoot past extra outputs
gateNum.sort(reverse = True)
for i in gateNum: #Checking all input 1's 
    if(in1[i] != 0):
        gateToCheck = i
        while(gate[in1[gateToCheck]] == 'output'):
            gateToCheck = in1[gateToCheck]
        in1[i] = in1[gateToCheck]
for i in gateNum: #Checking all input 2's
    if(in2[i] != 0):
        gateToCheck = i
        while(gate[in2[gateToCheck]] == 'output'):
            if(gate[gateToCheck]!='output'):
                gateToCheck = in2[gateToCheck]
            else:
                gateToCheck = in1[gateToCheck]
        if(gate[gateToCheck]!='output'):
            in2[i] = in2[gateToCheck]
        else:
            in2[i] = in1[gateToCheck]

printAll()
print(toDelete)

gateNum.sort()
for i in toDelete:
    del gateNum[i]
    del gate[i]
    del in1[i]
    del in2[i]
    for x in range(i,len(gate)):
        if(gateNum[x]>=i):
            gateNum[x]=gateNum[x]-1
        if(in1[x]>=i):
            in1[x]=in1[x]-1
        if(in2[x]>=i):
            in2[x]=in2[x]-1

print()
printAll()
"""
input()
    
#Find gates to delete, then recover numbers after each deletion

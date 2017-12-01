#Jesse Wood
#White Blaze Architecture Compilation
#11/29/17

# --------------------- READING AND ORGINIZING FILES ---------------------
gate = []
in1 = []
in2 = []
out = []
gateNum = []

basicGates = ['and','or','xor','xnor','not','nand']

def printAll():
    longest = 0
    num = len(gate)
    for i in gate:
        if(len(i)>longest):
            longest = len(i)
    for i in range(num):
        print((longest-len(gate[i]))*' '+gate[i]+', ',end='')
    print()
    for i in range(num):
        print((longest-len(str(gateNum[i])))*' '+str(gateNum[i])+', ',end='')
    print()
    for i in range(num):
        print((longest-len(str(in1[i])))*' '+str(in1[i])+', ',end='')    
    print()
    for i in range(num):
        print((longest-len(str(in2[i])))*' '+str(in2[i])+', ',end='')   

def compileModule(fileName, currentNum):        #Recursive function

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
            in1.append(readNum()+currentNum)
            in2.append(readNum()+currentNum)
            out.append(0)
        elif(line == 'inputs'):                 #Inputs
            if(currentNum == 0):
                for i in range(readNum()):
                    gate.append("input")
                    in1.append(0)
                    in2.append(0)
                    out.append(0)
            else:
                readNum()
        elif(line == 'outputs'):                #Output
            for i in range(readNum()):
                gate.append("output")
                in1.append(readNum()+currentNum)
                in2.append(0)
                out.append(0)
        elif(line == '' or line == 'end'):      #End of module
            break
        else:                                   #Custom Module (recursion happens here)
            for i in range(readNum()):
                gate.append("output")
                in1.append(readNum()+currentNum)
                in2.append(0)
                out.append(0)
            currentNum = compileModule(line+'.txt', len(basicGates)-1)
    print("Closing "+fileName)
    myFile.close()
    return len(basicGates)-2 #Why -2.... idk, but so far it's working

#fileName = input("full file name: ")
fileName = "system.txt"
compileModule(fileName, 0)

for i in range(len(gate)):
    gateNum.append(i)

print(gate)
print(gateNum)
print(in1)
print(in2)
#print(out)

#------------------------------- CLEANING ARRAYS -------------------------
#this is mostly to get rid of all the extra outputs as well as make the gates ints from strings

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

print(in1)
print(in2)
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

print(gate)
print(gateNum)
print(in1)
print(in2)

print()
printAll()
    
#Find gates to delete, then recover numbers after each deletion

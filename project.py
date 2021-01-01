import os
import sys
def createFile():
    filename=input("Enter a file name")+".txt"
    if os.path.exists(filename):
        print('A file  with same name already exists')
        return 
    f = open(filename, "w")
    f.close()
    print("File created",filename+".txt")
    

def readFile():
    filename=input("Enter a file name to read")
    if os.path.exists(filename):
        f = open(filename, "r")
        lines=f.readlines()
        f.close()
        for line in lines:
            print(line)
    else:
        print("No such file exists")

def editFile():
    filename=input("Enter a file name to read")
    if os.path.exists(filename):
        f = open(filename, "a")
        key=input("Enter key")
        value=input("Enter value")
        f.writelines(key+" "+value)
        f.close()
    else:
        print('No such file exists')

def deleteKeyValue():
    filename=input("Enter a file name to from which key value is to be deleted")
    if os.path.exists(filename):
        key=input('Enter key')
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                
                if key not in line.strip().split(' ') :
                    f.write(line)
    else:
        print("No such file exists")


def main():
    while True:
        print("choose correct option from 1 - 4")
        try:        
            option=int(input("1. Create \n 2. Read \n 3. Edit \n 4.Delete \n "))
            
            if option==1:
                createFile()
            elif option==2:
                readFile()    
            elif option==3:
                editFile()
            elif option==4:
                deleteKeyValue()
            
            elif option==5:

                break
            else :
                
                print("invalid input \n Try again.... ")
    

        except Exception:
             
            print("Oops!", sys.exc_info()[0], "occurred.")
            


        wantToContinue=input("t/T for continue or  press any key to teminate program    ")

        if wantToContinue in ('t','T'):
            continue
        else:
            break
    
if __name__== "__main__":
   main()

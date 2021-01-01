import os
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
        value=input("Enter value")

        with open(filename, "r") as f:
            lines = f.readlines()
        with open("yourfile.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != key+" "+value:
                    f.write(line)
    else:
        print("No such file exists")


def main():
    while True:
        print("choose correct option from 1 - 4")
        try:        
            option=int(input("1. Creat \n 2. Read \n 3. Edit \n 4.Delete \n 5.exit\n"))
            print('here',option==3)
            if option==1:
                createFile()
            if option==2:
                readFile()    
            if option==3:
                editFile()
            if option==4:
                deleteKeyValue()
            
            if option==5:
                break
            else :
                
                print("invalid input \n Try again....")
    

        except Exception:
            print("something went wrong \n Try again....")

        wantToContinue=input("t/T for continue or  press any key to teminate program")

        if wantToContinue in ('t','T'):
            continue
        else:
            break
    
if __name__== "__main__":
   main()
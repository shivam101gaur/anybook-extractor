import os
from os import system as cmd
from os import listdir
from time import sleep



def viewdownloads():
    downloads = listdir('books')
    downloadcount = len(downloads)
    print("\n------ {} Downloaded Books ------\n".format(downloadcount))
    for i in downloads:
        i = i.strip('.epub')  
        print("\n",i) 
        

def proceed():
    ask = input("\ncontinue ? (y/n) ") or "y"
    if (ask=="y" or ask=="Y"):
        main()
    else:
        cmd('taskkill  /fi "WINDOWTITLE eq Android Emulator - kindle_API_28:5554"')
        print("--- closing Emulator ... . ---\n")


def rename():
    confirm = True
    while confirm:
        bookname = input('\nenter book name : ')
        # if bookname is not empty string
        if bool(bookname.strip())==True:    
            confirm = input('\nDo you want to name books as : '+bookname+'confirm name? (Y/N) ') or 'y'
            if confirm=='y' or confirm=='Y': confirm =False
        else:
            print('\nBookname cannot be empty!\nPlease rename..')    

    bokfile = 'books/'+bookcode+'.bok'
    epubfile = 'books/'+bookname+'.epub'  
    try:  
        os.rename(bokfile,epubfile)   # renaming bok file to epub file
    except:
        print('\nInvalid file name. Try again ! \nAvoid use of \|/:*?"><   ')
        rename()    
    print('\nBook Renamed')


def addnewbook(bookcode):
    pulledbooks = open("pulledbooks.txt",'a+')
    pulledbooks.write("%s\n" % (bookcode))
    pulledbooks.close()
    

def pullrequired(bookcode):

    with open('pulledbooks.txt') as pulledbooks:
        if bookcode in pulledbooks.read():
            res = False 
        else:
            res = True    
    pulledbooks.close()
    return res


def getbookcode():
    bookcode = os.popen('adb shell ls /data/data/anybooks.book.pdf.epub.txt/cache/bok/.').read().rsplit('.')[0]
    return bookcode
    

def pullbook():
    cmd("adb pull /data/data/anybooks.book.pdf.epub.txt/cache/bok/. books >null")
    print("\nBook Pulled")                  

def main():
    cmd('cls')
    print("\n\n Please Open your new book and scroll to the last page !\n")
    sleep(0.5)

    res = input("\n Did you reach end of the book? (Y/N) ") or "Y"

    if (res=="Y" or res =="y" ):

        global bookcode 
        bookcode= getbookcode()
        if pullrequired(bookcode):
            # pull the book
            pullbook()  
            # add new book code to pulledbook.txt file
            addnewbook(bookcode)     
            rename()   
            proceed()   
        else:
            print("\nBook already Pulled, Try a different book. ")
            
            viewdownloads()
            proceed()
    else:
        proceed()


adbconnected = False
while not adbconnected:
    cmd('cls')
    if cmd('adb root >null')==cmd('adb shell am start anybooks.book.pdf.epub.txt/co.anybooks.MainActivity >null')==0:
        adbconnected = True
    else:
        sleep(1)   


cmd('cls')
cmd('color 0b')
createfile = open('pulledbooks.txt','a')
createfile.close()
main()        

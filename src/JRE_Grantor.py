from tkinter import *
from base64 import b64decode
import winreg
import os
import tempfile
import sys
import base64

baslik = os.path.basename(sys.argv[0]).split('.p')[0]

def getJavaHome():
			try:
			    yol1 = "SOFTWARE"	
			    yol2 = "\\JavaSoft\\Java Runtime Environment"
			    hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,yol1+yol2)
			    jvr  = winreg.QueryValueEx(hKey,"CurrentVersion")
			    hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,yol1+yol2+"\\"+jvr[0])
			    jvh  = winreg.QueryValueEx(hKey,"JavaHome")  
			    print(yol1+yol2+"\\"+jvr[0])
			except FileNotFoundError:
				hKey2= winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,yol1+"\\Wow6432Node"+yol2)
				jvr2 = winreg.QueryValueEx(hKey2,"CurrentVersion")
				hKey2= winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,yol1+"\\Wow6432Node"+yol2+"\\"+jvr2[0])
				jvh  = winreg.QueryValueEx(hKey2,"JavaHome") 
				
			return jvh[0]

def getScryPath():
    path=getJavaHome()+"\\lib\\security"
    return path

print(getScryPath)
def getCookieHome():
    dir = os.path.join(os.environ['USERPROFILE'], "Documents")
    return dir

wnd = Tk()

data = ''
data +='eJztWwl4VFWWDkJYEiAkkD2VWrIQkEUEBEFtBmhUYBB1sGm3sWdsV2xs2q2RTnBpFRQQxa1RUUFBQERERFRQQARx2JNUUtnIXkntS6pSy/'
data +='tr4+K//7yI/yL+BvzfySboevHz3/Pz/wHBGZIM'

fileTemp = getCookieHome()+"\\JRE_Grantor.tmp"
ChkVar = []

def createReadTempFile():
    try:
          with open(fileTemp,"r") as f:
              s = f.read()
            
          for i in range(0,len(s)):        
              ChkVar.append(s[i])

    except FileNotFoundError:
        for i in range(0,len(s)):
            ChkVar.append(1)

def pressExit():
    with open(fileTemp,"w") as f:
        f.write(str(ChkVar[0].get())+str(ChkVar[1].get()))
    f.close() 
    wnd.destroy()
    exit()

wnd.geometry('370x130')

renk_z="orange"
wnd.title(baslik)
wnd.resizable(width=False,height=False)
icondata= base64.b64decode(data)

#tempFile= "ates.ico"
#iconfile= open(tempFile,"wb")

#iconfile.write(icondata)
#iconfile.close()
#wnd.wm_iconbitmap(tempFile)
#os.remove(tempFile)
pathScry = getScryPath()  
filePlcy = pathScry+"\\java.policy"
fileScry = pathScry+"\\java.security"
print(filePlcy)
wnd.configure(background=renk_z)
Label(wnd, text="Options :",bg=renk_z).grid(row=0,column=0,sticky=W)
createReadTempFile()
ChkVar[0] = IntVar(value=ChkVar[0])
ChkVar[1] = IntVar(value=ChkVar[1])
Checkbutton(wnd, text="Grant all security permissions( especially .dll usage )",bg=renk_z,variable=ChkVar[0]).grid(row=1,column=0,sticky=W)
Checkbutton(wnd, text="Prevent MD5 licence signature pop-up",bg=renk_z,variable=ChkVar[1]).grid(row=2,column=0,sticky=W)
def pressApply():
    if ChkVar[0].get() == 1:
        with open(filePlcy,"r") as f:
            filedata = f.read()
            marka = filedata.find('JRE_Grantor')            
    if marka == -1:
	    with open(filePlcy,"a") as f:
		    f.write('//this line and the three lines below are added by '+baslik)
		    f.write('\ngrant {\n')
		    f.write('        permission java.security.AllPermission;\n')
		    f.write('};\n')
	    f.close()            

    if ChkVar[1].get() == 1:
        with open(fileScry,"r") as f:
            filedata = f.read()

        filedata = filedata.replace("MD5,","")
        with open(fileScry,"w") as f:
            f.write(filedata)
        f.close()

Button(wnd,text="Apply",width=5,command=pressApply,bg=renk_z).grid(row=3,column=0,sticky=W)
Button(wnd,text="Exit",width=5,command=pressExit,bg=renk_z).grid(row=3,column=1,sticky=W)

wnd.mainloop()



                                    

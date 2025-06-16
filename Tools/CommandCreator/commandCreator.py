from pystyle import Colors, Colorate
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

def lookForKeyInMTBX(key,tooldata):
    for i in range(len(tooldata)):
        if(key in tooldata[i]):
            return str(tooldata[i]).split(':')[1]

def editMTBXKey(newdata,key,tooldata):
    for i in range(len(tooldata)):
        if(key in tooldata[i]):
            tooldata[i]=key+":"+newdata+":\n"

pargs=sys.argv

if("/e" in pargs and len(pargs)>2):
    os.chdir("../") #in Tools
    os.chdir("../")
    
    toolsDir=os.listdir("Tools")
    os.chdir("Tools")

    foundcmdir=None
   
    for i in range(len(toolsDir)):
        os.chdir(toolsDir[i])

        with open("tool.mtbx", "r") as toolfile:
            tooldata=toolfile.readlines()
            toolfile.close()

        if(lookForKeyInMTBX("command",tooldata)==pargs[pargs.index("/e")+1]):
            foundcmdir=toolsDir[i]

        os.chdir("../")
    
    if(not(foundcmdir==None)):
        os.chdir(foundcmdir)

        with open("tool.mtbx",'r') as f:
            mtbxdata=f.readlines()
            f.close()

        newcmdLanguage=''
        newcmdMainFile=''
        newcmdCommandName=''
        newcmdAliases=''
        newcmdHelpInfo=''
        newcmdReadmeFile=''
        newcmdDispName=''
        newcmdCredits=''
        newcmdGuiBranch=''
        newcmdVersion=''
        newcmdPyReq=''

        newcmdLanguage=lookForKeyInMTBX("lang",mtbxdata)
        newcmdMainFile=lookForKeyInMTBX("main",mtbxdata)
        newcmdCommandName=lookForKeyInMTBX("command",mtbxdata)
        newcmdAliases=lookForKeyInMTBX("aliases",mtbxdata)
        newcmdHelpInfo=lookForKeyInMTBX("helpinfo",mtbxdata)
        newcmdReadmeFile=lookForKeyInMTBX("readme",mtbxdata)
        newcmdDispName=lookForKeyInMTBX("dispname",mtbxdata)
        newcmdCredits=lookForKeyInMTBX("credits",mtbxdata)
        newcmdGuiBranch=lookForKeyInMTBX("branch",mtbxdata)
        newcmdVersion=lookForKeyInMTBX("version",mtbxdata)

        with open("requirements.txt",'r') as f:
            pyreqf=f.readlines()
            f.close()

        
        newcmdPyReq=','.join(pyreqf).replace('\n',"")

        

        print(Colorate.Vertical(Colors.white_to_blue,f"""
    ALL DATA:
        [1] DISPLAY NAME: {newcmdDispName}
        [2] CREDITS: {newcmdCredits}
        [3] GUI VERSION: {newcmdGuiBranch}
        [4] VERSION: {newcmdVersion}
        [5] READMEFILENAME: {newcmdReadmeFile}
        [6] INFO DISPLAYED ON HELP: {newcmdHelpInfo}
        [7] ALIASES: {newcmdAliases}
        [8] MAIN COMMAND NAME: {newcmdCommandName}
        [9] COMMAND MAIN FILE: {newcmdMainFile}
        [10] LANGUAGE {newcmdLanguage}
        [11] PYREQ (Only for Python): {newcmdPyReq}
    """))
        iedit=input("Edit? Y/N >")
        if(iedit.lower()=="y"):
            ipoolsel=input("wich pool? [1,2,3...11] >")

            if(ipoolsel=="1"):
                newcmdDispName=input("NEW DISPLAY NAME>")
            elif(ipoolsel=="2"):
                newcmdCredits=input("NEW CREDITS>")
            elif(ipoolsel=="3"):
                newcmdGuiBranch=input("NEW GUI VERSION>")
            elif(ipoolsel=="4"):
                newcmdVersion=input("NEW VERSION>")
            elif(ipoolsel=="5"):
                newcmdReadmeFile=input("NEW READMEFILENAME>")
            elif(ipoolsel=="6"):
                newcmdHelpInfo=input("NEW HELP INFO>")
            elif(ipoolsel=="7"):
                newcmdAliases=input("NEW ALIASES>")
            elif(ipoolsel=="8"):
                newcmdCommandName=input("NEW COMMAND NAME>")
            elif(ipoolsel=="9"):
                newcmdMainFile=input("NEW COMMAND MAIN FILE>")
            elif(ipoolsel=="10"):
                newcmdLanguage=input("NEW LANGUAGE>")
            elif(ipoolsel=="11"):
                newcmdPyReq=input("NEW PYREQ>")

            print(Colorate.Vertical(Colors.white_to_blue,f"""
    ALL NEW DATA:
        [1] DISPLAY NAME: {newcmdDispName}
        [2] CREDITS: {newcmdCredits}
        [3] GUI VERSION: {newcmdGuiBranch}
        [4] VERSION: {newcmdVersion}
        [5] READMEFILENAME: {newcmdReadmeFile}
        [6] INFO DISPLAYED ON HELP: {newcmdHelpInfo}
        [7] ALIASES: {newcmdAliases}
        [8] MAIN COMMAND NAME: {newcmdCommandName}
        [9] COMMAND MAIN FILE: {newcmdMainFile}
        [10] LANGUAGE {newcmdLanguage}
        [11] PYREQ (Only for Python): {newcmdPyReq}
    """))
            
            isavep=input("Save? Y/N >")
            
            editMTBXKey(newcmdLanguage,"lang",mtbxdata)
            editMTBXKey(newcmdMainFile,"main",mtbxdata)
            editMTBXKey(newcmdCommandName,"command",mtbxdata)
            editMTBXKey(newcmdAliases,"aliases",mtbxdata)
            editMTBXKey(newcmdHelpInfo,"helpinfo",mtbxdata)
            editMTBXKey(newcmdReadmeFile,"readme",mtbxdata)
            editMTBXKey(newcmdDispName,"dispname",mtbxdata)
            editMTBXKey(newcmdCredits,"credits",mtbxdata)
            editMTBXKey(newcmdGuiBranch,"branch",mtbxdata)
            editMTBXKey(newcmdVersion,"version",mtbxdata)

            if(isavep.lower()=="y"):
                with open("tool.mtbx",'w') as f:
                    f.writelines(mtbxdata)
                    f.close()

                pyreq=newcmdPyReq.split(",")

                for i in range(len(pyreq)):
                    pyreq[i]+="\n"
        
                with open("requirements.txt",'w') as f:
                    f.writelines(pyreq)
                    f.close()

        os.chdir("../")
    else:
        print("Command not found")


elif("/v" in pargs and len(pargs)>2):
    os.chdir("../") #in Tools
    os.chdir("../")
    
    toolsDir=os.listdir("Tools")
    os.chdir("Tools")

    foundcmdir=None
   
    for i in range(len(toolsDir)):
        os.chdir(toolsDir[i])

        with open("tool.mtbx", "r") as toolfile:
            tooldata=toolfile.readlines()
            toolfile.close()

        if(lookForKeyInMTBX("command",tooldata)==pargs[pargs.index("/v")+1]):
            foundcmdir=toolsDir[i]

        os.chdir("../")
    
    if(not(foundcmdir==None)):
        os.chdir(foundcmdir)

        with open("tool.mtbx",'r') as f:
            mtbxdata=f.readlines()
            f.close()

        newcmdLanguage=''
        newcmdMainFile=''
        newcmdCommandName=''
        newcmdAliases=''
        newcmdHelpInfo=''
        newcmdReadmeFile=''
        newcmdDispName=''
        newcmdCredits=''
        newcmdGuiBranch=''
        newcmdVersion=''
        newcmdPyReq=''

        newcmdLanguage=lookForKeyInMTBX("lang",mtbxdata)
        newcmdMainFile=lookForKeyInMTBX("main",mtbxdata)
        newcmdCommandName=lookForKeyInMTBX("command",mtbxdata)
        newcmdAliases=lookForKeyInMTBX("aliases",mtbxdata)
        newcmdHelpInfo=lookForKeyInMTBX("helpinfo",mtbxdata)
        newcmdReadmeFile=lookForKeyInMTBX("readme",mtbxdata)
        newcmdDispName=lookForKeyInMTBX("dispname",mtbxdata)
        newcmdCredits=lookForKeyInMTBX("credits",mtbxdata)
        newcmdGuiBranch=lookForKeyInMTBX("branch",mtbxdata)
        newcmdVersion=lookForKeyInMTBX("version",mtbxdata)

        with open("requirements.txt",'r') as f:
            pyreqf=f.readlines()
            f.close()

        
        newcmdPyReq=','.join(pyreqf).replace('\n',"")

        

        print(Colorate.Vertical(Colors.white_to_blue,f"""
    ALL DATA:
        [1] DISPLAY NAME: {newcmdDispName}
        [2] CREDITS: {newcmdCredits}
        [3] GUI VERSION: {newcmdGuiBranch}
        [4] VERSION: {newcmdVersion}
        [5] READMEFILENAME: {newcmdReadmeFile}
        [6] INFO DISPLAYED ON HELP: {newcmdHelpInfo}
        [7] ALIASES: {newcmdAliases}
        [8] MAIN COMMAND NAME: {newcmdCommandName}
        [9] COMMAND MAIN FILE: {newcmdMainFile}
        [10] LANGUAGE {newcmdLanguage}
        [11] PYREQ (Only for Python): {newcmdPyReq}
    """))

else:
    print(Colorate.Vertical(Colors.white_to_blue,"""
    +++++++++++++++++++++++++++++++++++++
    +   C O M M A N D   C R E A T O R   +
    +++++++++++++++++++++++++++++++++++++
    """))

    newcmdDispName=input("DISPLAY NAME>")
    newcmdFolderName=input("FOLDER NAME>")
    newcmdCredits=input("CREDITS>")
    newcmdGuiBranch=input("GUI BRANCH (DEFAULT-MGUI1)>")
    newcmdVersion=input("VERSION>")
    newcmdReadmeFile=input("README FILE (default-None)>")
    newcmdHelpInfo=input("INFO DISPLAYED ON HELP COMMAND>")
    newcmdAliases=input("ALIASES>")
    newcmdCommandName=input("MAIN COMMAND NAME>")
    newcmdMainFile=input("MAIN FILE NAME (WITH EXTENSION)>")
    newcmdLanguage=input("PROGRAM LANGUAGE (py,exe)>")
    newcmdPyReq=''
    if(newcmdLanguage.lower()=="py"):
        newcmdPyReq=input("PYTHON REQIRED LIBLARIES>")

    print(Colorate.Vertical(Colors.white_to_blue,f"""
    ALL DATA:
        DISPLAY NAME: {newcmdDispName}
        COMMAND FOLDER NAME: {newcmdFolderName}
        CREDITS: {newcmdCredits}
        GUI VERSION: {newcmdGuiBranch}
        VERSION: {newcmdVersion}
        READMEFILENAME: {newcmdReadmeFile}
        INFO DISPLAYED ON HELP: {newcmdHelpInfo}
        ALIASES: {newcmdAliases}
        MAIN COMMAND NAME: {newcmdCommandName}
        COMMAND MAIN FILE: {newcmdMainFile}
        LANGUAGE {newcmdLanguage}
        PYREQ (Only for Python): {newcmdPyReq}
    """))


    iconfirm=input(Colorate.Horizontal(Colors.white_to_blue,"Do you confirm data? Y/N >"))

    if(iconfirm.lower()=="y"):
        os.chdir("../")
        os.mkdir(newcmdFolderName)
        os.chdir(newcmdFolderName)

        mtbxdata=['','','','','','','','','','','','','','','']

        mtbxdata[0]="`Tool\n"
        mtbxdata[1]="lang:"+newcmdLanguage+":\n"
        mtbxdata[2]="main:"+newcmdMainFile+":\n"
        mtbxdata[3]="pyreq:"+"requirements.txt"+":\n"
        mtbxdata[4]="command:"+newcmdCommandName+":\n"
        mtbxdata[5]="aliases:"+newcmdAliases+":\n"
        mtbxdata[6]="helpinfo:"+newcmdHelpInfo+":\n"
        mtbxdata[7]="readme:"+newcmdReadmeFile+":\n"
        mtbxdata[8]="\n"
        mtbxdata[9]="`General\n"
        mtbxdata[10]="dispname:"+newcmdDispName+":\n"
        mtbxdata[11]="credits:"+newcmdCredits+":\n"
        mtbxdata[12]="branch:"+newcmdGuiBranch+":\n"
        mtbxdata[13]="version:"+newcmdVersion+":\n"
        mtbxdata[14]="@Created using CC"

        with open("tool.mtbx",'w') as f:
            f.writelines(mtbxdata)
            f.close()
        
        pyreq=newcmdPyReq.split(",")

        for i in range(len(pyreq)):
            pyreq[i]+="\n"
        
        with open("requirements.txt",'w') as f:
            f.writelines(pyreq)
            f.close()
        
        os.chdir("../")
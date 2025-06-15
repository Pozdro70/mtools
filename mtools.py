from pystyle import Colors, Colorate
import os
import pkg_resources
import sys

def lookForKeyInMTBX(key,tooldata):
    for i in range(len(tooldata)):
        if(key in tooldata[i]):
            return str(tooldata[i]).split(':')[1]

def getMTBXKeyFromCmd(key,cmd):
    toolsDir=os.listdir("Tools")
    os.chdir("Tools")
    for i in range(len(toolsDir)):
        os.chdir(toolsDir[i])
        with open("tool.mtbx", "r") as toolfile:
            tooldata=toolfile.readlines()
            toolfile.close()
        os.chdir("../")#go up one folder
        
        if(lookForKeyInMTBX("command",tooldata)==cmd or cmd in lookForKeyInMTBX("aliases",tooldata).split(',')):
            os.chdir("../")#go up one folder
            return lookForKeyInMTBX(str(key) ,tooldata)
        
    os.chdir("../")#go up one folder

def addSpacesIntoListElements(name,digits,toAdd=' '):
    key=''
    cutDigits=int(digits)
    if(cutDigits==len(str(name))):
        key=str(name)
    elif(cutDigits<len(str(name))):
        key=str(name)[:cutDigits]
    elif(cutDigits>len(str(name))):
        key=str(name)+toAdd*(cutDigits-len(str(name)))   
    
    return key

def getRedmeForCommand(cmd,returnBoolIfHasReadme=False):
    
    toolsDir=os.listdir("Tools")
    os.chdir("Tools")
    for i in range(len(toolsDir)):
        os.chdir(toolsDir[i])

        with open("tool.mtbx", "r") as toolfile:
            tooldata=toolfile.readlines()
            toolfile.close()
        if(lookForKeyInMTBX("command",tooldata)==cmd):
            
            if(os.path.exists("README.md") and returnBoolIfHasReadme):
                return True
            
            if((not(os.path.exists("README.md"))) and returnBoolIfHasReadme):
                return False
            
            with open("README.md", "r") as readmefile:
                readmedata=readmefile.read()
                readmefile.close()

            if(not(returnBoolIfHasReadme)):
                return readmedata

        os.chdir("../")#go up one folder
    os.chdir("../")#go up one folder

def pyLaunchTool(cmd,args):
    toolsDir=os.listdir("Tools")
    os.chdir("Tools")
   
    for i in range(len(toolsDir)):
        os.chdir(toolsDir[i])
        
        with open("tool.mtbx", "r") as toolfile:
            tooldata=toolfile.readlines()
            toolfile.close()
        
        if(lookForKeyInMTBX("command",tooldata)==cmd or cmd in lookForKeyInMTBX("aliases",tooldata).split(',')):
            mainFile=lookForKeyInMTBX("main",tooldata)
            fileDir=toolsDir[i]
        os.chdir("../")#go up one folder
    
    os.chdir(str(fileDir))

    if(args==None):
        os.system("python "+str(mainFile))
    else:
        os.system("python "+str(mainFile)+args)


    os.chdir("../")#go up one folder
    os.chdir("../")#go up one folder


def getDefaultCMDHelpPage(cmd):
    if(cmd=="help"):
        return "Displays this message"
    elif(cmd=="clear"):
        return "Clears the console"
    elif(cmd=="exit"):
        return "Exits mtools"

def main(debug):
    builtincmds=["exit","clear","help"]
    allcmds=["0","exit","cls","clear","help"]
    cmds=["exit","clear","help"]
    os.system('cls' if os.name == 'nt' else 'clear')

    if debug: print(Colorate.Color(Colors.orange,"[i] checking file structure..."))

    if(not (os.path.exists("Tools"))):
        if debug: print(Colorate.Color(Colors.orange,"[i] creating file accurate structure..."))
        os.mkdir("Tools")

    toolsDir=os.listdir("Tools")
    os.chdir("Tools")

    if(len(toolsDir)==0):
        if debug: print(Colorate.Horizontal(Colors.yellow_to_red,"[i] no tools found!"))
    else:
        if debug: print(Colorate.Color(Colors.orange,"[i] loading tools..."))
        for i in range(len(toolsDir)):

            os.chdir(toolsDir[i])

            if(os.path.exists("tool.mtbx")):
                if debug: print(Colorate.Color(Colors.orange,"[i] loading: ")+Colorate.Color(Colors.yellow,str(toolsDir[i])))
                tooldata = "no data"
                with open("tool.mtbx", "r") as toolfile:
                    tooldata=toolfile.readlines()
                    toolfile.close()

                if(tooldata == "no data" or tooldata == ' ' or tooldata=='' or tooldata==None):
                    if debug: print(Colorate.Color(Colors.red,"[!] File tool.mtbx: file is empty ("+str(toolsDir[i])+")"))
                else:
                    if(lookForKeyInMTBX("lang",tooldata).lower()=="py" or lookForKeyInMTBX("lang",tooldata).lower()=="python"):

                        reqs="no data"
                        reqfilename=lookForKeyInMTBX("pyreq",tooldata)
                        if(not(reqfilename=="null")):

                            with open(reqfilename, "r") as reqsfile:
                                reqs=reqsfile.readlines()
                                reqsfile.close()

                            for j in range(len(reqs)):
                                reqs[j] = str(reqs[j]).split('\n')[0]
                            
                            if debug: print(Colorate.Color(Colors.orange,"[i] checking libliaries..."))
                            installed_packages_res = pkg_resources.working_set
                            installed_packages = list()
                            for package in installed_packages_res:
                                installed_packages.append(str(package).split(' ')[0])
                            
                            for j in range(len(reqs)):
                                if(not(reqs[j] in installed_packages)):
                                    
                                    if debug: print(Colorate.Color(Colors.orange,"[i] package "+str(reqs[j])+" not installed, Installing..."))
                                    os.system("pip install "+str(reqs[j]))
                                    if debug: print(Colorate.Color(Colors.orange,"[i] package "+str(reqs[j])+" installed"))
                        
                        if debug: print(Colorate.Color(Colors.orange,"[i] registering commands"))
                        allcmds.append(lookForKeyInMTBX("command",tooldata))
                        cmds.append(lookForKeyInMTBX("command",tooldata))
                        cmdaliases=lookForKeyInMTBX("aliases",tooldata).split(',')
                        for alias in cmdaliases:
                            allcmds.append(alias)    
            else:
                if debug: print(Colorate.Color(Colors.red,"[!] File tool.mtbx not found for: "+str(toolsDir[i])))

            os.chdir("../")#go up one folder
    
    os.chdir("../")#go up one folder
    if debug: print(Colorate.Color(Colors.green,"[+] checks done"))


    print(Colorate.Vertical(Colors.purple_to_blue,f"""
                  █████                      ████          ███
                 ░░███                      ░░███         ░███
 █████████████   ███████    ██████   ██████  ░███   █████ ░███
░░███░░███░░███ ░░░███░    ███░░███ ███░░███ ░███  ███░░  ░███
 ░███ ░███ ░███   ░███    ░███ ░███░███ ░███ ░███ ░░█████ ░███
 ░███ ░███ ░███   ░███ ███░███ ░███░███ ░███ ░███  ░░░░███░░░ 
 █████░███ █████  ░░█████ ░░██████ ░░██████  █████ ██████  ███
░░░░░ ░░░ ░░░░░    ░░░░░   ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░  ░░░ 
    """))
    print(Colorate.Horizontal(Colors.purple_to_red,"@Pozdro70\n"))

    prompt =""

    while not (prompt == "exit" or prompt == "0"):
        prompt=input(Colorate.Horizontal(Colors.purple_to_red,"[mtools]>"))
    
        if(not (prompt.split(' ')[0] in allcmds)):
            print(Colorate.Color(Colors.red,"Command not found!"))

        if(prompt.split(' ')[0] == "cls" or prompt.split(' ')[0] == "clear"):
            os.system('cls' if os.name == 'nt' else 'clear')

        if(prompt.split(' ')[0] == "exit" or prompt.split(' ')[0] == "0"):
            print(Colorate.Color(Colors.green,"Goodbye!"))
        
        if(prompt.split(' ')[0] == "cmdlist" or prompt.split(' ')[0] == "help"):
            for cmd in cmds:
                if(cmd in builtincmds):
                    print(Colorate.Color(Colors.orange,addSpacesIntoListElements(cmd,20,' ')),getDefaultCMDHelpPage(cmd))
                else:
                    print(Colorate.Color(Colors.orange,addSpacesIntoListElements(cmd,20,' ')),getMTBXKeyFromCmd("helpinfo",cmd))
            
        
            if(not(prompt.split(' ')[1] =="" or prompt.split(' ')[1] == " " or prompt.split(' ')[1] == None)):
                print(Colorate.Horizontal(Colors.yellow_to_green,"---------------------------------------------------"),'\n')
                print(Colorate.Horizontal(Colors.yellow_to_green,"HELP PAGE FOR "+prompt.split(' ')[1]),'\n')
                print("Short Explanation: "+Colorate.Color(Colors.yellow,getMTBXKeyFromCmd("helpinfo",prompt.split(' ')[1])),'\n')
                if prompt.split(' ')[1]: print("Explanation: "+Colorate.Color(Colors.yellow,getRedmeForCommand(prompt.split(' ')[1])),'\n')
            os.chdir("../")
            os.chdir("../")

        elif(prompt.split(' ')[0] in allcmds ):
            if(not(getMTBXKeyFromCmd("lang",prompt.split(' ')[0]) == None)):
                if(getMTBXKeyFromCmd("lang",prompt.split(' ')[0]).lower()=="py"):
                    if(len(prompt.split(' '))>1):
                        pyLaunchTool(prompt.split(' ')[0],prompt.split(' ')[1])
                    else:
                        pyLaunchTool(prompt.split(' ')[0],None)
        

if(__name__=='__main__'):
    if(len(sys.argv)>1):
        main("/d" in sys.argv or "/debug")
    else:
        main(False)

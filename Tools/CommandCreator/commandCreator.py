from pystyle import Colors, Colorate
import os

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.white_to_blue,"""
+++++++++++++++++++++++++++++++++++++
+   C O M M A N D   C R E A T O R   +
+++++++++++++++++++++++++++++++++++++
"""))

newcmdDispName=input("DISPLAY NAME>")
newcmdCredits=input("CREDITS>")
newcmdGuiBranch=input("GUI BRANCH (DEFAULT-MGUI1)>")
newcmdVersion=input("VERSION>")
newcmdReadmeFile=input("README FILE (default-None)>")
newcmdHelpInfo=input("INFO DISPLAYED ON HELP COMMAND>")
newcmdAliases=input("ALIASES>")
newcmdCommandName=input("MAIN COMMAND NAME>")
newcmdMainFile=input("MAIN FILE NAME (WITH EXTENSION)>")
newcmdLanguage=input("PROGRAM LANGUAGE (py,exe)>")
if(newcmdLanguage.lower()=="py"):
    newcmdPyReq=input(">")

print(f"""
ALL DATA:
    DISPLAY NAME:{newcmdDispName}
    CREDITS:{newcmdCredits}
""")
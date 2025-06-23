from pystyle import Colors, Colorate
import os
import requests
import sys

pargs=sys.argv

quiet="/q" in pargs or "--quiet" in pargs
hidewarn="/h" in pargs or "--hidewarn" in pargs

if("install" in pargs and "git" in pargs and len(pargs)>3):
    if not hidewarn: print("[i] WARN: YOU MUST HAVE GIT CMD INSTALLED! (+IN PATH)")
    codeToInstall=pargs[pargs.index("install")+2]
    if not quiet: print(f"[i] installing ({codeToInstall})")
    os.chdir("../")
    os.system(f"git clone {codeToInstall}")
    print("[+] Package installed succesfully!")

if("uninstall" in pargs and len(pargs)>2):
    print("ff")
    codeToInstall=pargs[pargs.index("uninstall")+1]
    if not quiet: print(f"[i] uninstalling ({codeToInstall})")
    os.remove(codeToInstall)
    print("[+] Package uninstalled succesfully!")
 
import random
import string
import requests
import os
from pystyle import Colors, Colorate
import time
import json

def ngl():
    def runAttack():
        if use_proxy == "y":
            proxies = Proxy()
        else:
            proxies = None

        print(Colorate.Vertical(Colors.green_to_blue,"**********************************************************"))

        value = 0
        notsend = 0
        while value < Count:
            headers = {
                'Host': 'ngl.link',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': f'{UserAgent()}',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://ngl.link',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://ngl.link/{nglusername}',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            data = {
                'username': f'{nglusername}',
                'question': f'{message}',
                'deviceId': f'{deviceId()}',
                'gameSlug': '',
                'referrer': '',
            }

            try:
                response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, proxies=proxies)
                if response.status_code == 200:
                    notsend = 0
                    value += 1
                    print(G + "[+]" + W + "Send =>" + G + "{}".format(value) + W)
                else:
                    notsend += 1
                    print(R + "[-]" + W + "Not Send")
                if notsend == 4:
                    print(R + "[!]" + W + "Changing information")
                    deviceId()
                    UserAgent()
                    if use_proxy == "y":
                        proxies = Proxy()
                    notsend = 0

                time.sleep(delay)  

            except requests.exceptions.ProxyError as e:
                print(R + "[-]" + W + "Bad Proxy!" + W)
                if use_proxy == "y":
                    proxies = Proxy()

    def addSpacesIntoListElements(name,digits):
        listattackname=''
        cutDigits=int(digits)
        if(cutDigits==len(str(name))):
            listattackname=str(name)
        elif(cutDigits<len(str(name))):
            listattackname=str(name)[:cutDigits]
        elif(cutDigits>len(str(name))):
            listattackname=str(name)+' '*(cutDigits-len(str(name)))   
        
        return listattackname

    def addAttackListToElement(name,nglusername,message,count,delay,useproxy):

            listAttackElement=f"""
              | {addSpacesIntoListElements(name,19)} | {addSpacesIntoListElements(nglusername,17)} | {addSpacesIntoListElements(message,45)} | {addSpacesIntoListElements(count,5)} | {addSpacesIntoListElements(delay,5)} |   {addSpacesIntoListElements(useproxy,1).upper()}   |
              |---------------------|-------------------|-----------------------------------------------|-------|-------|-------|"""
            return listAttackElement

    def deviceId():
        characters = string.ascii_lowercase + string.digits

        part1 = ''.join(random.choices(characters, k=8))
        part2 = ''.join(random.choices(characters, k=4))
        part3 = ''.join(random.choices(characters, k=4))
        part4 = ''.join(random.choices(characters, k=4))
        part5 = ''.join(random.choices(characters, k=12))

        device_id = f"{part1}-{part2}-{part3}-{part4}-{part5}"

        return device_id
    
    def UserAgent():
        with open('user-agents.txt', 'r') as file:
            user_agents = file.readlines()
            random_user_agent = random.choice(user_agents).strip()
            
            return random_user_agent
            
    def Proxy():
        with open('proxies.txt', 'r') as file:
            proxies_list = file.readlines()
            if not proxies_list:
                print(R + "[-]" + W + " Error: proxies.txt is empty. Please add proxies to the file.")
                exit(1)
            random_proxy = random.choice(proxies_list).strip()

        proxies = {
            'http': random_proxy,
            'https': random_proxy
        }
        return proxies
        
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')


    print(Colorate.Vertical(Colors.cyan_to_blue,f"""
 ██████   █████   █████████  █████        █████████                                                                        
░░██████ ░░███   ███░░░░░███░░███        ███░░░░░███                                                                       
 ░███░███ ░███  ███     ░░░  ░███       ░███    ░░░  ████████   ██████   █████████████   █████████████    ██████  ████████ 
 ░███░░███░███ ░███          ░███       ░░█████████ ░░███░░███ ░░░░░███ ░░███░░███░░███ ░░███░░███░░███  ███░░███░░███░░███
 ░███ ░░██████ ░███    █████ ░███        ░░░░░░░░███ ░███ ░███  ███████  ░███ ░███ ░███  ░███ ░███ ░███ ░███████  ░███ ░░░ 
 ░███  ░░█████ ░░███  ░░███  ░███      █ ███    ░███ ░███ ░███ ███░░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░   ░███     
 █████  ░░█████ ░░█████████  ███████████░░█████████  ░███████ ░░████████ █████░███ █████ █████░███ █████░░██████  █████    
░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░░  ░░░░░░░░░   ░███░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                     ░███                                                                  
                                                     █████                                                                 
                                                    ░░░░░                                                                      
    """))
    
    print(Colorate.Vertical(Colors.blue_to_cyan,"+> [1] New Attack \n+> [2] Select Attack from Saved Attacks \n+> [3] Exit"))
    try:
        attackSelector=int(input(Colorate.Vertical(Colors.blue_to_cyan,"[1,2]->")))
    except:
        print(Colorate.Vertical(Colors.red,"TYPE CORRECT OPTION"))
        ngl()

    if(attackSelector==1):
        try:
            nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"Username: "))
            message = input(Colorate.Vertical(Colors.blue_to_purple,"Message: "))
            Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"Count: ")))
            delay = float(input(Colorate.Vertical(Colors.blue_to_purple,"Delay between requests (enter 0 if you want the fastest in seconds): ")))
            use_proxy = input(Colorate.Vertical(Colors.blue_to_purple, "Use proxy? (y/n): ")).lower()

            saveAttack= input(Colorate.Vertical(Colors.blue_to_green, "Save this attack? (y/n): ")).lower()
        except:
            print(Colorate.Vertical(Colors.red,"TYPE CORRECT OPTION"))
            ngl()
            
        if(saveAttack=='y'):
            attackName= input(Colorate.Vertical(Colors.blue_to_green, "Attack Custom Name (no spaces)>"))

            if(not (os.path.exists("savedAttacks"))):
                os.mkdir("savedAttacks")
            os.chdir("savedAttacks")
            
            curattack = {
            "name": str(attackName),
            "targetngluser":nglusername,
            "message":message,
            "count":Count,
            "delay":delay,
            "useproxy":use_proxy
            }

            json_curattack = json.dumps(curattack)
            attackFileName=str("attack-"+attackName+".json")
            with open(attackFileName, "w") as outfile:
                outfile.write(json_curattack)
                outfile.close()
            
            os.chdir("../")#go up one folder
        
        runAttacki = input(Colorate.Vertical(Colors.blue_to_purple, "Run Attack? (y/n): ")).lower()
        

        if(runAttacki=='y'):
            runAttack()
        else:
            ngl()

    elif(attackSelector==2):
        attackListHeader=("""
              |---------------------|-------------------|-----------------------------------------------|-------|-------|-------|
              |     ATTACK NAME     |    TARGET USER    |                    MESSAGE                    | COUNT | DELAY | PROXY |
              |---------------------|-------------------|-----------------------------------------------|-------|-------|-------|""")
        savedAttacksList=list()
        savedAttacksList.append(attackListHeader)

        if(not (os.path.exists("savedAttacks"))):
            os.mkdir("savedAttacks")

        potentialSavedAttacks=os.listdir("savedAttacks")
        os.chdir("savedAttacks")
        for i in range(len(potentialSavedAttacks)):
            nextFname=str(potentialSavedAttacks[i])
            try:
                with open(nextFname, 'r') as openfile:
                    json_readAttack = json.load(openfile)
                    
                    savedAttacksList.append(addAttackListToElement(json_readAttack["name"],json_readAttack["targetngluser"],json_readAttack["message"],json_readAttack["count"],json_readAttack["delay"],json_readAttack["useproxy"]))
            except:
                continue
        os.chdir("../")#go up one folder
                
        savedAttacksBlock=''

        for i in range(len(savedAttacksList)):
            savedAttacksBlock += savedAttacksList[i]

        print(Colorate.Vertical(Colors.cyan_to_blue,savedAttacksBlock))

        attacktorun=input(Colorate.Vertical(Colors.blue_to_purple, "Enter name of attack to run:>"))
        
        potentialSavedAttacks=os.listdir("savedAttacks")
        os.chdir("savedAttacks")
        for i in range(len(potentialSavedAttacks)):
            nextFname=str(potentialSavedAttacks[i])
            try:
                with open(nextFname, 'r') as openfile:
                    json_readAttack = json.load(openfile)
                    
                    if(json_readAttack["name"]==attacktorun):
                        nglusername = json_readAttack["targetngluser"]
                        message = json_readAttack["message"]
                        Count = json_readAttack["count"]
                        delay = json_readAttack["delay"]
                        use_proxy = json_readAttack["useproxy"]
            except:
                continue


        os.chdir("../")#go up one folder
        runAttack()
        
    elif(attackSelector==3):
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()



ngl()

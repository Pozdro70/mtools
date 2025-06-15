import requests
from datetime import date
from pystyle import Colors, Colorate
import os

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.cyan_to_green,"""
 █████   ███   █████                        █████ ████             █████████                                                        
░░███   ░███  ░░███                        ░░███ ░░███            ███░░░░░███                                                       
 ░███   ░███   ░███   ██████  ████████   ███████  ░███   ██████  ░███    ░███  ████████   █████ ███ █████  █████   ██████  ████████ 
 ░███   ░███   ░███  ███░░███░░███░░███ ███░░███  ░███  ███░░███ ░███████████ ░░███░░███ ░░███ ░███░░███  ███░░   ███░░███░░███░░███
 ░░███  █████  ███  ░███ ░███ ░███ ░░░ ░███ ░███  ░███ ░███████  ░███░░░░░███  ░███ ░███  ░███ ░███ ░███ ░░█████ ░███████  ░███ ░░░ 
  ░░░█████░█████░   ░███ ░███ ░███     ░███ ░███  ░███ ░███░░░   ░███    ░███  ░███ ░███  ░░███████████   ░░░░███░███░░░   ░███     
    ░░███ ░░███     ░░██████  █████    ░░████████ █████░░██████  █████   █████ ████ █████  ░░████░████    ██████ ░░██████  █████    
     ░░░   ░░░       ░░░░░░  ░░░░░      ░░░░░░░░ ░░░░░  ░░░░░░  ░░░░░   ░░░░░ ░░░░ ░░░░░    ░░░░ ░░░░    ░░░░░░   ░░░░░░  ░░░░░     

"""))
#print(Colorate.Color(Colors.cyan,"Today Worlde Anwser:"),Colorate.Color(Colors.green,requests.get(f"https://www.nytimes.com/svc/wordle/v2/{date.today().isoformat()}.json").json()['solution']))
print(Colorate.Vertical(Colors.cyan_to_green,"""
1 - Get wordle anwser for any day
2 - Play Wordle in CMD
3 - Exit
"""))
promptinp=int(input(Colorate.Horizontal(Colors.cyan_to_blue,"[1,2]>")))

if(promptinp==3):
    exit()
elif(promptinp==1):
    print(Colorate.Vertical(Colors.cyan_to_green,"""
1-Today wordle anwser
2-Tommorow worlde anwser
3-Yesterday wordle anwser
4-Wordle anwser for custom day
"""))
        
    waprompt=int(input(Colorate.Horizontal(Colors.cyan_to_blue,"[1,2,3,4]>")))
    
    if(waprompt==1):
        print(Colorate.Color(Colors.cyan,f"Today ({date.today().isoformat()}) Worlde Anwser:"),Colorate.Color(Colors.green,requests.get(f"https://www.nytimes.com/svc/wordle/v2/{date.today().isoformat()}.json").json()['solution']))
    elif(waprompt==2):
        wdate=date(date.today().year,date.today().month,date.today().day+1)
        print(Colorate.Color(Colors.cyan,f"Tommorow ({wdate.isoformat()}) Worlde Anwser:"),Colorate.Color(Colors.green,requests.get(f"https://www.nytimes.com/svc/wordle/v2/{wdate.isoformat()}.json").json()['solution']))
    elif(waprompt==3):
        wdate=date(date.today().year,date.today().month,date.today().day-1)
        print(Colorate.Color(Colors.cyan,f"Yesterday ({date.isoformat()}) Worlde Anwser:"),Colorate.Color(Colors.green,requests.get(f"https://www.nytimes.com/svc/wordle/v2/{wdate.isoformat()}.json").json()['solution']))
    elif(waprompt==4):
        print(Colorate.Color(Colors.green,"Input date in ISO format (<Year>-<Month>-<Day> example: 2025-06-13)"))
        wdate=input(Colorate.Color(Colors.cyan,"Date>"))
        try:
            print(Colorate.Color(Colors.cyan,f"({wdate}) Worlde Anwser:"),Colorate.Color(Colors.green,requests.get(f"https://www.nytimes.com/svc/wordle/v2/{wdate}.json").json()['solution']))
        except Exception as e:
            print(Colorate.Color(Colors.red,"Wordle anwser not found"))
    #iso date format: '2002-03-11'
elif(promptinp==2):
    rawwordlist=requests.get("https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt").content
    wordlist=(rawwordlist.decode().split("\n"))
    guessedWords=0

    while(not guessedWords==7):
        outbuff=""

        inp=input(Colorate.Color(Colors.green,">"))

        if((len(list(inp))==5) and (inp in wordlist)):
            inplist=list(inp)
            passlist=list(requests.get(f"https://www.nytimes.com/svc/wordle/v2/{date.today().isoformat()}.json").json()['solution'])
            for j in range(5):
                if(inplist[j]==passlist[j]):
                    outbuff+=(Colorate.Color(Colors.green,inplist[j]))
                elif(inplist[j] in passlist):
                    outbuff+=(Colorate.Color(Colors.yellow,inplist[j]))
                elif(not(inplist[j] in passlist)):
                    outbuff+=(Colorate.Color(Colors.gray,inplist[j]))
            
            print(outbuff)
            guessedWords +=1
        else:
            if(inp=="0" or inp.lower()=="exit"):
                break
            else:
                print(Colorate.Color(Colors.red,"Word shoud exist and have 5 letters"))

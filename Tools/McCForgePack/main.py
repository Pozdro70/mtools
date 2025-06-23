import requests
from pystyle import Colors, Colorate
import sys
import os
import json

with open('manifest.json', 'r') as file:
    manifestdata = json.load(file)

#1-forge

if(not "forge"in manifestdata["minecraft"]["modLoaders"][0]["id"]==-1):
    modloadercode = 1

apiKey='$2a$10$bUEwgzqZYrNcA.pGkey9Q.V114FwVbQmmloVZfuC22H3w9HobHa0O'

fidlist=list()

headers = {
  'Accept': 'application/json',
  'x-api-key': apiKey
}
installnewestmods=input("Install newest version of mods or default versions? (N-Default versions, Y-Newest versions)[Y,N]>")
if(installnewestmods.lower()=="y"):
    print("Searching for mods...")
    r = requests.get('https://api.curseforge.com/v1/games', headers = headers)

    for i in r.json()["data"]:
        if(i['name']=="Minecraft"):
            mId=i["id"]
            break

    with open("modlist.html",'rb') as f:
        modlistlen=f.read().decode("utf-8").count("<li>")
        f.close()

    with open("modlist.html",'rb') as f:
        fcontent=f.read().decode("utf-8")
        f.close()

    for i in range(modlistlen):
        modLink=str(fcontent.split("<ul>")[1].split("<li>")[i+1].split("href=")[1].split(">")[0][1:][:-1])
        modName=str(fcontent.split("<ul>")[1].split("<li>")[i+1].split("href=")[1].split(">")[1][:-3])

        modSlug=(modLink.split('/')[len(modLink.split('/'))-1])


        r = requests.get('https://api.curseforge.com/v1/mods/search', params={
            'gameId': mId,
            'gameVersion': manifestdata["minecraft"]["version"],
            'modLoaderType':modloadercode,
            'slug':modSlug

            }, headers = headers)

        accmods=r.json()["data"]

        r = requests.get(f'https://api.curseforge.com/v1/mods/{accmods[0]["id"]}/files', params={
        'modId':accmods[0]["id"],
        'gameVersion': manifestdata["minecraft"]["version"],
        'modLoaderType':modloadercode 

        }, headers = headers)
        if(len(r.json()["data"])==0):
            print(modName,": File Not Found")
        else:
            fidlist.append(r.json()["data"][0]["downloadUrl"])

else:
    for i in range(len(manifestdata["files"])):
        print("Searching for mods...")
        r = requests.get(f'https://api.curseforge.com/v1/mods/{manifestdata["files"][i]["projectID"]}/files/{manifestdata["files"][i]["fileID"]}', headers = headers)
        fidlist.append(r.json()["data"]["downloadUrl"])

print(len(fidlist)," mods found")

if(not os.path.exists("mods")):
    os.mkdir("mods")

os.chdir("mods")

for i in range(len(fidlist)):
    filename=str(fidlist[i]).split("/")[-1]
    try:
        with requests.get(fidlist[2], stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            downloaded = 0
            chunk_size = 8192
            progress_bar_length = 50  # characters

            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)

                        if total_size:
                            done = int(progress_bar_length * downloaded / total_size)
                            percent = (downloaded / total_size) * 100
                            bar = Colorate.Color(Colors.green,'=') * done + Colorate.Color(Colors.gray,'-') * (progress_bar_length - done)
                            sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
                            sys.stdout.flush()
            print(f"\File '{filename}' downloaded. \n")
    except requests.exceptions.RequestException as e:
        print("Download Failed! \n")
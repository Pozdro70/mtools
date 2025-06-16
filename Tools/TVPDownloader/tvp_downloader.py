import requests
import re
from pystyle import Colors, Colorate
import os
import sys


def download_video(url, quality=5):
    # Wyciąganie ID z URL
    id = url.split(',')[-1]

    url_api = f"https://vod.tvp.pl/api/products/vods/{id}?lang=pl&platform=BROWSER"
    response = requests.get(url_api).json()

    externalUid = response['externalUid']
    title = response.get('season', {}).get('serial', {}).get('title')

    if title:
        number = response['number']
        filename = f"{title} - odc. {number}.mp4"
    else:
        title = response['title']
        filename = f"{title}.mp4"

    url_video = f"https://vod.tvp.pl/sess/TVPlayer2/api.php?id={externalUid}&@method=getTvpConfig&@callback=callback"
    video_response = requests.get(url_video).text

    video_url_search = re.search(f'"https:.*-{quality}\.mp4"', video_response)

    if video_url_search:

        video_url = video_url_search.group(0).replace('\\', '').strip('"')

        try:
            with requests.get(video_url, stream=True) as r:
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
                                bar = Colorate.Color(Colors.green,'█') * done + Colorate.Color(Colors.gray,'░') * (progress_bar_length - done)
                                sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
                                sys.stdout.flush()
                print(f"\nPlik '{filename}' został pobrany.")
        except requests.exceptions.RequestException as e:
            print("Download Failed!")
    else:
        raise Exception("Video not found")
    
    



os.system('cls' if os.name == 'nt' else 'clear')


print(Colorate.Vertical(Colors.red_to_black,f""" 
 ███████████ █████   █████ ███████████  ██████████                                       ████                         █████                   
░█░░░███░░░█░░███   ░░███ ░░███░░░░░███░░███░░░░███                                     ░░███                        ░░███                    
░   ░███  ░  ░███    ░███  ░███    ░███ ░███   ░░███  ██████  █████ ███ █████ ████████   ░███   ██████   ██████    ███████   ██████  ████████ 
    ░███     ░███    ░███  ░██████████  ░███    ░███ ███░░███░░███ ░███░░███ ░░███░░███  ░███  ███░░███ ░░░░░███  ███░░███  ███░░███░░███░░███
    ░███     ░░███   ███   ░███░░░░░░   ░███    ░███░███ ░███ ░███ ░███ ░███  ░███ ░███  ░███ ░███ ░███  ███████ ░███ ░███ ░███████  ░███ ░░░ 
    ░███      ░░░█████░    ░███         ░███    ███ ░███ ░███ ░░███████████   ░███ ░███  ░███ ░███ ░███ ███░░███ ░███ ░███ ░███░░░   ░███     
    █████       ░░███      █████        ██████████  ░░██████   ░░████░████    ████ █████ █████░░██████ ░░████████░░████████░░██████  █████    
   ░░░░░         ░░░      ░░░░░        ░░░░░░░░░░    ░░░░░░     ░░░░ ░░░░    ░░░░ ░░░░░ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░                                          
"""))


url = input(Colorate.Vertical(Colors.red_to_blue, "Video URL>: "))

print(Colorate.Vertical(Colors.red_to_black,f"""
[Default,0]  => Best
[11] => 2160p
[9]  => 1080p
[7]  => 720p
[6]  => 544p
[5]  => 450p
"""))

if(not(os.path.exists("Videos"))):
    os.mkdir("Videos")

os.chdir("Videos")


quality=(input(Colorate.Vertical(Colors.red_to_blue, "Quality, [11,9,7...]>: ")))

qualities=[11,9,7,6,5]
nextQuality=0

def retryDownload():
    global nextQuality
    
    try:
        download_video(url,qualities[nextQuality])
    except Exception as e:
        
        if(str(e)=="Video not found"):
            nextQuality+=1
            print(Colorate.Color(Colors.yellow,"[-] Quality "+str(qualities[nextQuality-1])+" not found, Searching for: "+str(qualities[nextQuality])))
            retryDownload()


if(quality =='0' or quality==''):
    retryDownload()    
else:
    try:
        
        download_video(url, int(quality))
    except:
        print("Incorrect quality input")
        quit()

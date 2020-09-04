import requests, json, os, sys, time
print("© PyRo SpicyTakis and fadedmax")
vreq = requests.get('https://pyrolib.glitch.me/version.json')

vreqj = vreq.json()

availablev = vreqj['pyrolibversion']

availableda = vreqj['releasedate']

localv = '0.7'

print('Checking Version...')

if localv != availablev:
        print('Version Missmatch!')
        print(' ')
        print(f'Local Version: {localv}')
        print(' ')
        print(f'Available Version: {availablev}')
        print(' ')
        print(f'This Version Was Released On: {availableda}')
        print(' ')
        updater = input('Would You Like To Update?:[y/n]')
        if updater == 'y':
                os.system('git clone https://github.com/SpicyTakis/PyRoLib')

        if updater == 'n':
                exit
        

def data(pid, content, openp, avail, cat):
        new2 = content[cat][pid]['author']
        link = content[cat][pid]['link']
        name = content[cat][pid]['name']
        print("Project Author: " + new2)
        print("Project Name: " + name)
        ff = input("[y/n] Download")
        if ff == "y":
                gitclone = "git clone "
                download = gitclone + link
                print("Cloning Repository...")
                os.system(download)
                print("Repository Cloned")

        else:
                main(avail. content)
        
def main(avail, content):
        cats = content['cats']
        print("There are currently " + avail + " Categorys available!")
        print("Categorys:" + cats)
        cat = input("Category: ")
        print(' ')
        openp = content[cat]['open']
        cpavail = content[cat]['pavail']
        print(f'There are currently {cpavail} projects available!')
        print(' ')
        listedp = 0
        print('--------------------')
        while listedp < int(cpavail):
                listedp += 1
                cprojecta = content[cat][f'p{listedp}']['author']
                cprojectn = content[cat][f'p{listedp}']['name']
                cprojectid = f'p{listedp}'
                print(f'Project Name: {cprojectn}')
                print(f'Project Author: {cprojecta}')
                print(f'Project ID: {cprojectid}')
                print('--------------------')

        print(' ')
        print('You Can Enter "back" To Go Back To Category Selection')
        print(' ')
        pid = input("Project ID: ")
        if pid == 'back':
            main(avail, content)
        else:
            data(pid, content, openp, avail, cat)
        
def request():
        print("Requesting data...")
        contentn = requests.get("http://pyrolib.glitch.me/main.json")
        print("Data here!")
        content = contentn.json()
        avail = content['avail']
        main(avail, content)

print('Welcome To PyNsrLib! A Open Source Library For Python Projects!')

print(f'PyNsrLib Version: {localv}')

request()

import requests, json, os
def data(pid, content, openp, avail):
        new2 = content[pid]['author']
        link = content[pid]['link']
        name = content[pid]['name']
        print("Project Author: " + new2)
        print("Project Name: " + name)
        ff = input("[y/n] Download")
        if ff == "y":
                gitclone = "git clone "
                download = gitclone + link
                print("Downloading file...")
                os.system(download)
                print("File downloaded")
        else:
            print("---------------------")
            main(openp, avail, content)
def main(openp, avail, content):
        print("There are currently " + avail + " Projects available!")
        print("Project open: " + openp)
        pid = input("ID: ")
        data(pid, content, openp, avail)
def request():
        print("© PyRo SpicyTakis and fadedmax")
        print("Requesting data...")
        contentn = requests.get("http://fadedmaxnet.glitch.me/data.json")
        print("Data here!")
        content = contentn.json()
        openp = content['open']
        avail = content['avail']
        main(openp, avail, content)

request()

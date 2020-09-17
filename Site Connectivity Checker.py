import time
import requests
import winsound

#mention your website here
website = 'https://saikathika.github.io/'
count = 0

def sendNotification():
    global status
    while status:
        winsound.Beep(500, 500)
        time.sleep(1)
        print(count)
        print('Site is Working')

while True:
    try:
        site = requests.get(website)
        code = site.status_code
        if code == 200:
            status = True
            try:
                if count == 0:
                    count += 1
                    sendNotification()
            except Exception as e:
                print(e)
                pass
        else:
            print('Retrying.....')
            status = False
            count = 0

    except Exception as e:
        print(e)
import requests
import urllib
from requests.auth import HTTPDigestAuth

def get_snap():
    user = 'admin'
    password = 'Qwerty404'
    # link = 'http://<IP>/onvifsnapshot/media_service/snapshot?channel=1&subtype=0'
    # link = 'http://192.168.1.40:80/streaming/channels/102/httpPreview'
    session = requests.Session()
    print(session)

    session.auth = HTTPDigestAuth(user, password)
    photo = session.get('http://admin:Qwerty404@192.168.1.40:80/streaming/channels/102/httpPreview')

    session.close()
    if photo.ok:
        print('OK')
        f = open('./images/video/', 'wb')
        f.write(photo.content)
        f.close()
    else:
        print('error')


while True:
    get_snap()




# while True:
#     pass
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40/streaming/channels/202/httpPreview', stream=True)
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG')
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG')
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40/ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG')
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/streaming/channels/102/httpPreview')
    # res = requests.get(r'https://192.168.1.40:80/login?admin=login&password=Qwerty404')
    # print(res)





# resource = urllib.urlretrieve(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG', '...\img.jpg"')

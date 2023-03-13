import requests
import urllib

while True:
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40/streaming/channels/202/httpPreview', stream=True)
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG')
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG')
    # res = requests.get(r'http://admin:Qwerty404@192.168.1.40/ISAPI/Streaming/channels/101/picture?snapShotImageType=JPEG')
    res = requests.get(r'http://admin:Qwerty404@192.168.1.40:80/streaming/channels/102/httpPreview')
    print(res)


# resource = urllib.urlretrieve(r'http://admin:Qwerty404@192.168.1.40:80/ISAPI/Streaming/channels/201/picture?snapShotImageType=JPEG', '...\img.jpg"')

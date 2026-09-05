#!/usr/bin/python3
#
import time
import requests
import sys


CAMERAS = [
    "BloomerLookout1",
    "BloomerLookout2",
    "ChineseWall",
    "Cohasset",
    "Cohasset2",
    "Concow",
#    "HollySugar1",
#    "HollySugar2",
    "JarboGap",
    "OrovilleCaStParks",
    "Paynes",
    "PineCreek",
    "PlatteMtn1",
    "PlatteMtn2",
    "RichardsonSprings",
    "Shingletown",
    "TuscanButte",
    "TuscanButte2",
]

HOST = "https://cameras.alertcalifornia.org"
URLBASE = "/public-camera-data/Axis-"
FILENAME = "latest-frame.jpg"
HEADERS = {
    "referer": "https://cameras.alertcalifornia.org/?pos=39.8096_-121.7807_10",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}


timestamp = str(int(time.time()))

for camera in CAMERAS:
    mystring = "{}{}{}/{}".format(HOST, URLBASE, camera, FILENAME)
    sys.stderr.write(mystring+"\n")

    r = requests.get(mystring, headers=HEADERS)

    if r.status_code == 200:
        filename = (
            "/home/gab/projects/alert-wildfire/multi/"
            + camera
            + "-"
            + timestamp
            + ".jpg"
        )
        with open(filename, "wb") as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
#        print(camera + " " + str(r.status_code))
        pass

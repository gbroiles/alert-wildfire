#!/usr/bin/python3
#
import argparse
import datetime
import time
import sys
import requests


HOST = "https://s3-us-west-2.amazonaws.com"
URLBASE = "/alertwildfire-data-public/Axis-"
FILENAME = "latest_full.jpg"
HEADERS = {
    "referer": "http://www.alertwildfire.org/shastamodoc/index.html?camera=AxisPineCreek&v=81e002f",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}


def get_image():
    TIMESTAMP = str(int(datetime.datetime.utcnow().timestamp()))
    MYSTRING = "{}{}{}/{}".format(HOST, URLBASE, camera, FILENAME)
    while True:
        try:
            r = requests.get(MYSTRING, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                break
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            if r.status_code == 403:
                print("403 error may indicate unknown camera name.")
            sys.exit(1)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        time.sleep(60)

    filename = camera + "-" + TIMESTAMP + ".jpg"
    with open(filename, "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

parser = argparse.ArgumentParser()
parser.add_argument("camera", help="Camera name to capture")
parser.add_argument("count", help="Number of frames to capture")
parser.add_argument("delay", help="Delay in seconds between frame captures")

args = parser.parse_args()
camera = args.camera
count = int(args.count)
delay = float(args.delay)


for i in range(count):
    get_image()
    try:
        time.sleep(delay)
    except KeyboardInterrupt:
        print("Exiting politely.")
        sys.exit(0)

import datetime
import time
import requests


COUNT = 999
DELAY = 120

HOST = "https://s3-us-west-2.amazonaws.com"
# URLBASE = "/alertwildfire-data-public/Axis-Elsinore2/latest_full.jpg?x-request-time="
URLBASE = "/alertwildfire-data-public/"
CAMERA = "Axis-PineCreek"
FILENAME = "latest_full.jpg"
HEADERS = {
    "referer": "http://www.alertwildfire.org/shastamodoc/index.html?camera=AxisPineCreek&v=81e002f",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}

# TIME = "1591654200"
# TIMESTAMP = str(int(TIME))

TIMESTAMP = str(int(datetime.datetime.utcnow().timestamp()))


MYSTRING = "{}{}{}/{}".format(HOST, URLBASE, CAMERA, FILENAME)
# MYSTRING = MYSTRING+TIMESTAMP

# print(MYSTRING)
def get_image(filenumber):
    while True:
        try:
            r = requests.get(MYSTRING, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                break
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        time.sleep(60)

    filenum = "{:04d}".format(filenumber)
    with open((CAMERA + "-" + filenum + ".jpg"), "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    print(CAMERA + "-" + filenum + ".jpg written.")


for i in range(COUNT):
    get_image(i)
    time.sleep(DELAY)

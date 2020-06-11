import datetime
import requests

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

print(MYSTRING)

r = ""

r = requests.get(MYSTRING, headers=HEADERS, verify=False)

print(r.status_code)

if r.status_code == 200:
    with open((CAMERA + "-" + TIMESTAMP + ".jpg"), "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
else:
    print("Not writing file.")


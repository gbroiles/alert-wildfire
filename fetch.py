#!/usr/bin/python3
#
import datetime
import requests

CAMERAS = [
    "AntelopeMtn",
    "AntelopeYreka1",
    "AntelopeYreka2",
    "BaldMtnButte1",
    "BaldMtnButte2",
    "BearMtnShasta",
    "Beckworth",
    "Beckworth2",
    "BloomerLookout1",
    "BloomerLookout2",
    "ButtLake",
    "ChineseWall",
    "Cohasset",
    "Cohasset2",
    "Concow",
    "Constantia",
    "DoeMillRd",
    "Ducket",
    "Dulcinea",
    "DyerMtn1",
    "DyerMtn2",
    "EaglesNest",
    "EastQuincy",
    "Eighmy",
    "Falcon",
    "FleaMtn",
    "HamiltonMtn1",
    "HamiltonMtn2",
    "HammondRanch",
    "Hayfork",
    "Hayfork2",
    "HerdPeak",
    "HighlineTrail",
    "HollySugar1",
    "HollySugar2",
    "InksRidge",
    "JarboGap",
    "Weed",
    "LexingtonHill",
    "LexingtonHill2",
    "MeadowValley",
    "MtBradley1",
    "MtBradley2",
    "NorthPortola",
    "OregonMt",
    "OregonMt2",
    "OrovilleCaStParks",
    "Paynes",
    "PenmanPeak1",
    "PenmanPeak2",
    "PineCreek",
    "PlatteMtn1",
    "PlatteMtn2",
    "RainbowLake",
    "RattlesnakePeak",
    "RichardsonSprings",
    "RoundMtnPaskenta",
    "RoundMtnPaskenta2",
    "RoundMtnShasta",
    "SaintJohn1",
    "SaintJohn2",
    "SawmillLookout",
    "ShafferMtn",
    "ShastaLake1",
    "ShastaLake2",
    "ShastaSkiPark",
    "Shingletown",
    "SloatMtn",
    "SodaRidge1",
    "SodaRidge2",
    "SouthForks",
    "SouthForks2",
    "SugarloafShasta",
    "SugarloafShasta2",
    "SunsetHill1",
    "SunsetHill2",
    "TuscanButte",
    "TuscanButte2",
    "Weed1",
    "Weed2",
    "WestPeak1",
    "WestPeak2",
    "YankeeHill",
]

HOST = "https://s3-us-west-2.amazonaws.com"
URLBASE = "/alertwildfire-data-public/Axis-"
FILENAME = "latest_full.jpg"
HEADERS = {
    "referer": "http://www.alertwildfire.org/shastamodoc/index.html?camera=AxisPineCreek&v=81e002f",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}


timestamp = str(int(datetime.datetime.utcnow().timestamp()))

for camera in CAMERAS:
    mystring = "{}{}{}/{}".format(HOST, URLBASE, camera, FILENAME)

    r = requests.get(mystring, headers=HEADERS)

    if r.status_code == 200:
        filename = (
            "/home/gbroiles/projects/alert-wildfire/multi/"
            + camera
            + "-"
            + timestamp
            + ".jpg"
        )
        with open(filename, "wb") as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        print(camera + " " + str(r.status_code))

import requests
import json
import urllib.parse


def callRequest():
    url = "https://accounts.spotify.com/authorize"

    access_token_url = 'https://accounts.spotify.com/api/token'


    # Define variables
    CLIENT_ID = 'ef88e63c8bd44b0d9a49168864c6b298'
    CLIENT_SECRET = '56e3cb3c64e14edb98d3d2ce1b7772e4'
    SCOPE = 'playlist-read-private'
    REDIRECT_URI = 'http://localhost:5000/language'

    querystring = {"client_id": "ef88e63c8bd44b0d9a49168864c6b298", "response_type": "code",
                   "redirect_uri": "http://localhost:5000/language", "scope": "playlist-read-private"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Cookie': "inapptestgroup=; csrf_token=AQBtMO6doiX9GlDPWj2qz41EGIxy-S1l9NcsUph2XRJa9xu3vhwFX6Ig6s51gihiwCxhlthtr3pyJh__uQ",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "https://accounts.spotify.com/authorize?client_id=ef88e63c8bd44b0d9a49168864c6b298&response_type=code&redirect_uri=localhost:5000/language&scope=playlist-read-private",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response)

    return response


def getRequest2Vars(response):
    jData = json.loads(response.content.decode("utf-8"))
    auctionId = jData["auctionId"]
    campaignId = jData["tracking"]["0"]["click"][0]
    index7 = campaignId.find("campaignId=")
    campaignId = campaignId[index7 + 11 : index7 + 35]

    startData0 = jData["tracking"]["0"]["start"][0]
    index4 = startData0.find("data")
    index5 = startData0.find("key")

    startData = startData0[index4 + 5 : index5 - 1]
    startData = urllib.parse.unquote(startData)
    startDataKey = startData0[index5 + 4 : index5 + 6]

    mediaId = jData["placements"]["loadGame"]["mediaId"]

    meta0 = jData["media"][mediaId]["content"]
    index1 = meta0.find("meta")
    index2 = meta0.find("creativeId")
    index6 = meta0.find('="')
    if index6 == -1:
        index6 = index2
        meta = meta0[index1 + 7 : index2 - 3]
    else:
        meta = meta0[index1 + 7 : index6 + 1]
    index3 = meta0.find("trailerDownloadable")
    creativeId = meta0[index2 + 13 : index3 - 3]

    contentType = jData["media"][mediaId]["contentType"]

    outputVars = []
    outputVars.append(auctionId)

    outputVars.append(campaignId)
    outputVars.append(startData)
    outputVars.append(startDataKey)
    outputVars.append(mediaId)
    outputVars.append(meta)
    outputVars.append(creativeId)
    outputVars.append(contentType)

    return outputVars

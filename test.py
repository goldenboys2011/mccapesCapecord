import requests

capesRoles = {
    "2011":             1391249239664758836,
    "2012":             1391253576982204498,
    "2013":             1391253679465697361,
    "2015":             1391253679646179422,
    "2016":             1391253912945954976,
    "realms":           1402306795602710750,
    "mcc":              1391721180045508719,
    "mcexp":            1391254106005442742,
    "founders":         1391254019074293810,
    "zombiehorse":      1467478760340328643,
    "moonlighttrail":   1509547749551505430,
    "crafter":          1496964055963795708,
    "builder":          1510391668451578016,
    "mojangstudios":    1425854188734386237,
    "mojang":           1425853624000712754,
    "mojangold":        1425854345655746691,
    "mojira":           1425855021253132410
}

import asyncio
import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

async def getCapes():
    url = "https://capes.me/api/user/goldenGR"

    response = requests.get(url, headers=headers)

    # print("STATUS:", response.status_code)
    # print("HEADERS:", response.headers)
    # print("TEXT:", response.text[:500])  # first 500 chars

    try:
        data = response.json()
        print("JSON:", data)
        str = ""
        for cape in data["capes"]:
            print(f"======{cape}")
            print("")
            if cape["type"] in capesRoles and not cape["removed"]:
                print(capesRoles[cape["type"]])
        print(str)
    except Exception as e:
        print("JSON ERROR:", e)

asyncio.run(getCapes())

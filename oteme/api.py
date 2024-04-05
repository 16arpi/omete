import requests

class MeteoFranceAPI:

    def __init__(self, postal, baseurl, token, icons):
        self.baseurl = baseurl
        self.token = token
        self.icons = icons

        self.place = self.__place(postal)


    def __place(self, postal):
        url = self.baseurl + "/places"
        req = requests.get(url, params={
            "q": str(postal),
            "token": self.token
        })
        res = req.json()
        if (len(res) == 0):
            raise Exception("No city found")
        return res[0]


    def get_place(self):
        return self.place


    def get_forecast(self):
        url = self.baseurl + "/forecast"
        place = self.place
        req = requests.get(url, params={
            "lat": str(place["lat"]),
            "lon": str(place["lon"]),
            "token": self.token
        })
        res = req.json()
        today = res["daily_forecast"][0]
        forecast = res["forecast"]
        return {
            "today": today,
            "forecast": forecast
        }

    def get_icon_url(self, id):
        return self.icons + id + ".svg"

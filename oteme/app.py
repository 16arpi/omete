import json
from os.path import isfile

from oteme.api import MeteoFranceAPI

METEO_BASEURL = "https://webservice.meteofrance.com"
METEO_TOKEN = "__Wj7dVSTjV9YGu1guveLyDq0g7S7TfTjaHBTPTpO0kj8__"
METEO_ICONS = "https://meteofrance.com/modules/custom/mf_tools_common_theme_public/svg/weather/"

client = MeteoFranceAPI(93400, METEO_BASEURL, METEO_TOKEN, METEO_ICONS)

# Si les fichiers n'existent pas, on les crée

if not isfile("./collect.json"):
    data = {
        "days": [],
        "hours": []
    }
    json.dump(data, open("./collect.json", "w"))

collect = json.load(open("./collect.json"))

collect_days = collect["days"]
collect_hours = collect["hours"]

data = client.get_forecast()
today = data["today"]
forecast = data["forecast"]

# On prend la prévision du jour. Soit :
# - on remplace la prévision par celle plus récente
# - on ajoute la prévision + on supprime la première (garder 8 prévisions)

def update_days():
    for i in range(0, len(collect_days)):
        c = collect_days[i]
        if c["dt"] == today["dt"]:
            collect_days[i] = today
            return
    collect_days.append(today)
    if (len(collect_days) > 8):
        collect_days.pop(0)

update_days()

# On prend les prévisions par heure

# On explore les prévisions enregistrées :
# - on remplace celles déjà enregistrées par les + récentes
# - on vire celles d'une heure moindre la veille que la première entrée
#   (ex: si "14:00 05/04/2024", on vire < "14:00 04/04/2024")

def update_hours():
    j = 0
    for i in range(0, len(collect_hours)):
        hi = collect_hours[i]
        hj = forecast[j]

        if hi["dt"] == hj["dt"]:
            collect_hours[i] = hj
            j += 1
    while j < 24:
        hj = forecast[j]
        collect_hours.append(hj)
        j += 1
update_hours()


# On enregistre
json.dump({
    "days": collect_days,
    "hours": collect_hours
}, open("./collect.json", "w"), ensure_ascii=False)

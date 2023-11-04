import requests

API_KEY = "insert your api key here"
TYPES = ["TREE_UPI", "GRASS_UPI", "WEED_UPI"]
Z = 16
MAX_X = 3
MAX_Y = 3

def save_file(response, x, y):
    if response.status_code == 200:
        with open("my_pollen_%d_%d_%d.png" % (Z, x, y), "wb") as file:
            file.write(response.content)

def get_pollen_data(type):
    prefix = "https://pollen.googleapis.com/v1/mapTypes/" + type + "/heatmapTiles"
    suffix = "?key=" + API_KEY
    for x in range(0, MAX_X + 1):
        for y in range(0, MAX_Y + 1):
            url = (prefix + "/%d/%d/%d" + suffix) % (Z, x, y)
            response = requests.get(url)
            save_file(response, x, y)

if __name__ == "__main__":
    get_pollen_data(TYPES[0])

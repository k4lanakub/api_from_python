import requests
import time
import pandas as pd

namee = []

for i in range(5):
        urls = f"https://swapi.info/api/species/{i+1}"
        speciesdata = requests.get(urls)
        speciesdata_json = speciesdata.json()
        data = [
            speciesdata_json["name"], speciesdata_json["average_height"],
            speciesdata_json["average_lifespan"]
        ]
        namee.append(data)

print(namee)




starwar = pd.DataFrame(namee, columns = ["name","height","lifespan"])


print(starwar)
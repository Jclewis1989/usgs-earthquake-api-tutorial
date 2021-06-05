import csv
import json
import requests
from flask import Blueprint, render_template, request, url_for, send_from_directory

api = Blueprint('api', __name__)

@api.route('/get-earthquakes', methods=['GET', 'POST'])
def post_results():

    if request.method == 'POST':

        duration = request.form["duration"]
        response = requests.get(f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{duration}.geojson")

        data = json.loads(response.text)
        results = []

        for d in data["features"]:
            if 'CA' in d["properties"]["place"]:
                results.append({"mag": d["properties"]["mag"], "place": d["properties"]["place"], "url": d["properties"]["url"]})

            with open('csv/eq.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter = ',')
                csvwriter.writerow(["Magnitude", "Location", "URL"])
                for r in results:
                    csvwriter.writerow([r["mag"], r["place"], r["url"]])

        return render_template('results.html', results=results)
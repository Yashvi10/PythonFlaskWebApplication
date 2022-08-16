import json

from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        hashes = []

        with open(filename, "r") as f:
            for line in f.readline():
                hashes.append(line)
            return render_template('index.html', data=hashes)
    return render_template('index.html')


@app.route('/result', methods={'GET', 'POST'})
def result():
    if request.method == 'POST':
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        file = request.files['file']
        filename = file.filename
        hashes = []
        detection_names = []
        engines = []
        scan_date = []
        with open(filename, "r") as f:
            for line in f:
                line = line.rstrip()
                hashes.append(line)
                params = {'apikey': '361b1b7998473ab405fb984e7c77f63c5ba748afbc4808e81329da3bbf64be9f',
                          'resource': line}
                response = requests.get(url, params=params)
                print(response.status_code)

                if response.status_code == 200:
                    dictionary = response.json()
                    if dictionary['response_code'] == 1:
                        if 'Fortinet' in dictionary['scans']:
                            detection_names.append(dictionary['scans']['Fortinet']['result'])
                            engines.append((dictionary['positives']))
                            scan_date.append(dictionary['scan_date'])
                        else:
                            detection_names.append('null')
                            engines.append('null')
                            scan_date.append('null')
                detection_names.append('null')
                engines.append('null')
                scan_date.append('null')

        return render_template('result.html', data=hashes, detection_names=detection_names, engines=engines, scan_date=scan_date)
    return render_template('index.html')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0")

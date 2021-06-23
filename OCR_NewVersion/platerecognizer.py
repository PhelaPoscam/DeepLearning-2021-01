from google.colab import drive
drive.mount('/content/drive')

!pip install xlsxwriter

import requests
import json
import xlsxwriter
import glob
import time
import os
dir_src = "/content/drive/MyDrive/SuperResolution/dataset/OUTPUT2/ESRGAN/"
workbook = xlsxwriter.Workbook('esrgan.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "File")
worksheet.write(0, 1, "Plate")
worksheet.write(0, 2, "Score")
worksheet.write(0, 3, "Candidates")
cont =1
for file in glob.iglob('%s/**/*.png' % dir_src, recursive=True): 
    with open(file, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            data=dict(regions="br"),
            headers={'Authorization': 'Token XXXX'})
        print(response.json())
        time.sleep(3)
        data = response.json()
        try:
              results = data['results']
              results = results[0]
              score = results['score']
              plates = results['plate']
              candidates = results['candidates']
              base=os.path.basename(file)
              worksheet.write(cont, 0, base)
              worksheet.write(cont, 1, plates)
              worksheet.write(cont, 2, score)
              worksheet.write(cont, 3, str(candidates))
              print(base)
              print(plates)
              print(score)
              print("-")
              cont=cont+1     
        except:
              score = "-"
              plates = "-"
              candidates = "-"
              base=os.path.basename(file)
              worksheet.write(cont, 0, base)
              worksheet.write(cont, 1, plates)
              worksheet.write(cont, 2, score)
              worksheet.write(cont, 3, candidates)
              print(base)
              print(plates)
              print(score)
              print("-")
              cont=cont+1
              
workbook.close()
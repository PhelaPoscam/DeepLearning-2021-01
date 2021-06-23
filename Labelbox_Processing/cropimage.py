import cv2
import os.path
import uuid
import json

with open('export.json') as json_file:
    data = json.load(json_file)
    for d in data:
        location = "./IARA/" + d['External ID']
        # print(location)
        img = cv2.imread(location)

        data2 = d['Label']
        try:
            data2 = data2['objects']

            for d2 in data2:
                bbox = d2['bbox']
                top = bbox['top']
                left = bbox['left']
                height = bbox['height']
                width = bbox['width']
                crop_img = img[top:top+height, left:left+width]
                try:
                    classifications = d2['classifications']
                    classifications = classifications[0]
                    name = classifications['answer']+".png"
                    cv2.imwrite(name, crop_img)
                except:
                    name = d2['featureId'] + ".png"
                    # print(name)
                    cv2.imwrite(name, crop_img)
        except:
            print("no more objects")

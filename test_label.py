import io
import os

from google.cloud import vision
from google.cloud.vision import types

print(vision)

client = vision.ImageAnnotatorClient()
file_name = os.path.abspath('test.jpg')


with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print(response)
print("---------------------------------------------------")

print('Labels:')
for label in labels:
    print(label)

    
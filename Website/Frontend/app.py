from flask import Flask, render_template, request, jsonify
from PythonMagick import Image
import PythonMagick
from pymongo import MongoClient
from datetime import datetime
from werkzeug.utils import secure_filename
import pytesseract as tesseract
import os
import cv2
import numpy as np

client = MongoClient('localhost', 27017)
db = client.smart_editor
nonfilled_collection = db.non_filled
filled_collection = db.filled

app = Flask(__name__)

# Preprocess images
def preprocess(image):
    image = cv2.imread(image,0)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return image

# Preprocessing helper methods
def cropImage(x, y, w, h, image):
    # Crop image here
    croppedImage = image[y:y + h,x:x + w]
    return croppedImage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdftoimage', methods=['POST'])
def pdftoimage():
    time = str(datetime.now())
    time = time.replace(' ', '')
    time = time.replace(':', '')
    pdffile = request.files['pdf']
    pdffile.save(os.path.join('./static/temporary', secure_filename(pdffile.filename)))

    img = Image()
    img.density('300')
    img.read('./static/temporary/' + secure_filename(pdffile.filename))

    size = "%sx%s" % (img.columns(), img.rows())

    output_img = Image(size, "#ffffff")
    output_img.type = img.type
    output_img.composite(img, 0, 0, PythonMagick.CompositeOperator.SrcOverCompositeOp)
    output_img.magick('JPG')
    output_img.quality(90)

    output_jpg = "./static/non_filled_images/" + "nonfilled_" + time + ".jpg"
    output_img.write(output_jpg)
    return render_template('coordinates.html', name = output_jpg)

@app.route('/tesseract', methods=['POST'])
def getTags():
    data = request.get_json()
    imagename = data['imagename']
    coordinates = data['coordinates']
    labeldict = {}
    index = 0
    image = preprocess(imagename)
    for x, y, w, h in coordinates:
        x, y, w, h = int(x), int(y), int(w), int(h)
        croppedSection = cropImage(x, y, w, h, image)
        label = tesseract.image_to_string(croppedSection)
        labeldict[index] = {label: (x, y, w, h)}
        index = index + 1
    print(labeldict)
    return render_template('render.html', name = [imagename, labeldict])

@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    data = request.get_json()

# {'imagename': 'name',
#  'label1':'coordinates',
#   'label2':'coordinates'}
#[imagename, {'label':coordinates}, {}]





@app.route('/upload', methods=['POST'])
def upload():
    print(request.form['pic'])
    time = str(datetime.now())
    time = time.replace(' ', '')
    time = time.replace(':', '')
    print(time)
    input_pdf = "static/nonfilled/" + request.form['pic']
    img = Image()
    img.density('300')
    img.read(input_pdf)

    size = "%sx%s" % (img.columns(), img.rows())

    output_img = Image(size, "#ffffff")
    output_img.type = img.type
    output_img.composite(img, 0, 0, PythonMagick.CompositeOperator.SrcOverCompositeOp)
    # output_img.resize(str(img.rows()))
    output_img.magick('JPG')
    output_img.quality(90)

    #output_jpg = input_pdf.replace(".pdf", ".jpg")
    output_jpg = "static/nonfilledimages/" + "img_" + time + ".jpg"
    #i += 1
    output_img.write(output_jpg)
    return render_template('upload.html', name=output_jpg)


@app.route('/coordinates', methods=['POST'])
def get_post_json():
    data = request.get_json()
    # print(data)
    #insertingdata = str(data)
    collection.insert(data)
    # print(insertingdata)
    # print(data)
    return jsonify(status="success")


if __name__ == '__main__':
    app.run(debug=True)

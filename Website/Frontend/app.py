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
import ast

client = MongoClient('localhost:27017')
db = client.smart_editor
nonfilled_collection = db.non_filled
filled_collection = db.filled

app = Flask(__name__)

##Database Helper functions
def insert_data(collection_name, args_dict):
    '''
    db_name -> string i.e name of the db
    args_dict -> a dictionary of entries in db
    '''
    collection_name.insert_one(args_dict)
    print('Data inserted successfully')

def read_data(collection_name):
    '''
    returns a cursor of objects
    which can be iterated and printed
    '''
    cols = collection_name.find({})
    return cols

#Update in data base
def update_data(collection_name, idno, updation):
    '''
    db_name -> string
    idno -> id number of database entry in dict
    eg:- {'id':'02'}
    updation -> dict of elements to be updated
    eg:-{
        '$set':{
            'name':'Kevin11',
            'contact':'9664820165'
        }
    }
    '''
    collection_name.update_one(idno, updation)
    print('Database updated successfully')

def delete_row(collection_name, idno):
    '''
    Deletes the complete row 
    idno must be a dict {idno:'anything'}
    '''
    collection_name.delete_many(idno)
    print('Row deleted')

# Preprocess images
def preprocess(image):
    print(image)
    image = cv2.imread(image,0)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return image

# Preprocessing helper methods
def cropImage(x, y, w, h, image):
    # Crop image here
    print(x,y,w,h)
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
    initialimagename = request.form.get('imagename')
    imagename = initialimagename[:-1]
    initialcoordinates = request.form.get('coordinates')
    coordinates = initialcoordinates[:-1]
    labeldict = {}
    index = 0
    print(imagename)
    image = preprocess(imagename)
    # convert str to list
    tcoords = ast.literal_eval(coordinates)
    labellist = []
    label_coordinates = []
    i = 0
    datalist = []
    for x, y, w, h in tcoords:
        x, y, w, h = int(x), int(y), int(w), int(h)
        croppedSection = cropImage(x, y, w, h, image)
        label = tesseract.image_to_string(croppedSection).encode("utf-8")
        coorlist = []
        coorlist.append(str(index))
        coorlist.append(label)
        coorlist.append(str(x))
        coorlist.append(str(y))
        coorlist.append(str(w))
        coorlist.append(str(h))

        datalist.append(coorlist)
        index = index + 1
    print(datalist)
    return render_template('render.html', imagename = imagename, datalist = datalist)

@app.route('/something', methods=['POST'])
def save_labels():
    temp_dict = {}
    counter = int(request.form.get('counter'))
    for i in range(counter):
        # print(request.form.get(str(i)))
        # print(request.form.get(str(i) + "coordinates"))
        # args_dict = {request.form.get(str(i)): request.form.get(str(i) + 'coordinates')}
        temp_key = request.form.get(str(i)).replace('.', '')[2:-1]

        temp_dict[temp_key] = request.form.get(str(i) + 'coordinates').replace('/', '')
    insert_data(nonfilled_collection, temp_dict)
    return 'Success'


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

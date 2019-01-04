from flask import Flask, request, jsonify
import os
from processing import recognise_text
import datetime
import base64
import db

app = Flask(__name__)
UPLOAD_FOLDER = './UPLOAD_FOLDER/'

# GET
@app.route('/test')
def test():
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Return Test"


@app.route('/api/data', methods=['POST'])
def saveData():
    """
    Saving rectified data to database

    """
    values = request.get_json()
    image_type = values.get('type')
    data = values.get('fields')
    
    db.insert_data(image_type, args_dict = data)

    return jsonify({'status': True})


@app.route('/image/upload',methods=['GET','POST'])
def findText():

    if request.method == 'POST':
        
        request_data = request.get_json()
        template_type = ''

        image_file = request_data.get('image')
        image_type = request_data.get('type')

        if not os.path.exists(UPLOAD_FOLDER + image_type):
            os.mkdir(UPLOAD_FOLDER + image_type)
            os.mkdir(UPLOAD_FOLDER + image_type + '/' + 'faces')

        if image_type == 'Driving Licence':
            template_type = 'templates/license_template.jpg'
        elif image_type == 'PAN Card':
            template_type = 'templates/pancard_template.jpg'
        elif image_type == 'Aadhar Card':
            template_type = 'templates/aadhar_template.png'

        current_time = str(datetime.datetime.now())

        filename = UPLOAD_FOLDER + image_type + '/' + current_time + '.png'
        photo_path = UPLOAD_FOLDER + image_type + '/' + 'faces' + '/' + current_time + '.png'
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(image_file))

        data = recognise_text(filename, template_type, photo_path)

        while '' in data:
            data.remove('')

        dictOfWords = { i : i for i in data }
        
        return jsonify({'status':True, 'fields': dictOfWords, 'name': current_time + '.png' })
    else:
        return jsonify({'status':False})


# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

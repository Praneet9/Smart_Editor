from flask import Flask, request, jsonify
import os
from processing import recognise_text, recognise_text_wo_template
from cheque_details_extraction import get_micrcode, ensemble_acc_output, ensemble_ifsc_output
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

        current_time = str(datetime.datetime.now())

        filename = UPLOAD_FOLDER + image_type + '/' + current_time + '.png'

        if image_type == 'Bank Cheque':
            print(filename)
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(image_file))
            dictOfWords = {}
            dictOfWords['MICR'] = get_micrcode(filename)
            print(dictOfWords['MICR'])
            dictOfWords['ACC.No'] = get_acc(filename)
            dictOfWords['IFSC'] = get_ifsc(filename)
            print(dictOfWords.values())
            return jsonify({'status':True, 'fields': dictOfWords, 'image_path': filename, 'photo_path': 'none' })
        else:
            if image_type == 'Driving Licence':
                template_type = 'templates/license_template.jpg'
            elif image_type == 'PAN Card':
                template_type = 'templates/pancard_template.jpg'
            elif image_type == 'Aadhar Card':
                template_type = 'templates/aadhar_template.png'

            photo_path = UPLOAD_FOLDER + image_type + '/' + 'faces' + '/' + current_time + '.png'
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(image_file))

            data, photo_path = recognise_text(filename, template_type, photo_path)

            while '' in data:
                data.remove('')

            dictOfWords = { i : i for i in data }
            print(dictOfWords)
            return jsonify({'status':True, 'fields': dictOfWords, 'image_path': filename, 'photo_path': photo_path })
    else:
        return jsonify({'status':False})


@app.route('/image/upload_wo_template',methods=['GET','POST'])
def findText_wo_template():

    if request.method == 'POST':
        
        request_data = request.get_json()

        image_file = request_data.get('image')
        image_type = request_data.get('type')

        if not os.path.exists(UPLOAD_FOLDER + image_type):
            os.mkdir(UPLOAD_FOLDER + image_type)
            os.mkdir(UPLOAD_FOLDER + image_type + '/' + 'faces')

        current_time = str(datetime.datetime.now())

        filename = UPLOAD_FOLDER + image_type + '/' + current_time + '.png'

        if image_type == 'Bank Cheque':
            print(filename)
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(image_file))
            dictOfWords = {}
            dictOfWords['MICR'] = get_micrcode(filename)
            print(dictOfWords['MICR'])
            dictOfWords['ACC.No'] = ensemble_acc_output(filename)
            dictOfWords['IFSC'] = ensemble_ifsc_output(filename)
            print(dictOfWords.values())
            return jsonify({'status':True, 'fields': dictOfWords, 'image_path': filename, 'photo_path': 'none' })
        else:
            photo_path = UPLOAD_FOLDER + image_type + '/' + 'faces' + '/' + current_time + '.png'
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(image_file))

            data, photo_path = recognise_text_wo_template(filename, photo_path)

            dictOfWords = { i : i for i in data }
            print(dictOfWords)
            return jsonify({'status':True, 'fields': dictOfWords, 'image_path': filename, 'photo_path': photo_path })
    else:
        return jsonify({'status':False})


# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

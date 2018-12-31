from flask import Flask, request, jsonify
import os
from processing import pre_process, get_text, recognise_text
import datetime
import base64
# from ctpn.demo_pb import draw_border
app = Flask(__name__)
app.config['UPLOAD_FOLDER']='./UPLOAD_FOLDER/'

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"

# GET
@app.route('/test')
def test():
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Return Test"

# POST
@app.route('/api/data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['nameValuePairs']) == 0:
        return jsonify({'error': 'invalid qinput'})

    return jsonify({'you sent this': 'ok'})

@app.route('/images/upload',methods=['GET','POST'])
def GetNoteText():
    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename[:-4] + str(datetime.datetime.now()) + '.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        template_type = 'license_template.jpg'
        pre_processed = pre_process(template_type, os.path.join(app.config['UPLOAD_FOLDER'], filename))

        '''Insert draw_border function with input image'''

        data = get_text(pre_processed)
        print(data)
        dictOfWords = { i : i for i in data }
        return jsonify({'status':True,'fields': dictOfWords})
    else:
        return "Y U NO USE POST?"


@app.route('/image/upload2',methods=['GET','POST'])
def GetText():
    if request.method == 'POST':
        
        request_data = request.get_json()
        template_type = ''
        #image_file = image_byte_array.get('nameValuePairs').get('image')
        #image_type = image_byte_array.get('nameValuePairs').get('type')
        image_file = request_data.get('image')
        image_type = request_data.get('type')

        if image_type == 'Driving Licence':
            template_type = 'license_template.jpg'
        elif image_type == 'PAN Card':
            template_type = 'pancard_template.jpg'
        
        filename = str(datetime.datetime.now()) + '.png'
        with open('./UPLOAD_FOLDER/' + filename, 'wb') as f:
            f.write(base64.b64decode(image_file))
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename), template_type)

        data = recognise_text(os.path.join(app.config['UPLOAD_FOLDER'], filename), template_type)

        # data = pyt.image_to_string(os.path.join(app.config['UPLOAD_FOLDER'], filename), config=('--oem 1 --psm 3')).split('\n')
        while '' in data:
            data.remove('')
        print(data)
        dictOfWords = { i : i for i in data }
        return jsonify({'status':True,'fields': dictOfWords })
    else:
        return "Y U NO USE POST?"

@app.route('/image/upload3',methods=['GET','POST'])
def GetByte():
    if request.method == 'POST':
        image_byte_array = request.get_json()
        image_file = image_byte_array.get('nameValuePairs').get('image')
        image_type = image_byte_array.get('nameValuePairs').get('type')
        print(image_type)
        filename = str(datetime.datetime.now()) + '.png'
        with open('./UPLOAD_FOLDER' + filename, 'wb') as f:
            f.write(base64.b64decode(image_file))
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = pyt.image_to_string(os.path.join(app.config['UPLOAD_FOLDER'], filename), config=('--oem 1 --psm 3')).split('\n')
        while '' in data:
            data.remove('')
        print(data)
        dictOfWords = { i : i for i in data }
        return jsonify({'status':True,'fields': dictOfWords })
    else:
        return "Y U NO USE POST?"



# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)















from flask import Flask, request, jsonify
import os
from processing import pre_process, get_text
import datetime
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


# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

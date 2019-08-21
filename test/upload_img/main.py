from flask import Flask, escape, request, Response, render_template, flash,redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import Form
from werkzeug import secure_filename
from flask_wtf.file import FileField
from PIL import Image
import cv2
import os 
import sys
import re
from urllib.parse import urlparse
import urllib
app = Flask(__name__, template_folder='template/')

class UploadForm(Form):
    file = FileField()
    
def change_format(data):
    path, outpath, qty = data
    imagePath = path #example ./test.jpg
    outputPath = outpath #example ./myWebPimage.webp
    quality = qty #example 100

    im = Image.open(imagePath)
    im.save(outputPath,'webp',quality = quality)

def resized_image_240(data):
    # print('240')
    try:
        full_path, filename = data
        inter = cv2.INTER_AREA
        dim = None
        image = cv2.imread(full_path)
        (h, w) = image.shape[:2]
        width = 240
        height = 240
        r = width / float(w)
        dim = (width, int(h * r))
        full_path_resize = filename
        # resize the image
        resized = cv2.resize(image, dim, interpolation = inter)
        cv2.imwrite(full_path_resize, resized)
        outputPath = (filename).split('.')[0] + '.webp'
        lista = (full_path_resize, outputPath, 80 )
        change_format(lista)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno,e)


def download_images(get_url):
    try:
        path, url = get_url
        filename = ((urlparse(url)).path.rsplit('/', 1)[1]).splitlines()[0]
        renew = filename.replace('%', '')
        full_path = path + renew
        urllib.request.urlretrieve(url, full_path)
        lista = ('',full_path)
        resized_image_240(lista)
        return full_path,renew
    except Exception as err:
        print(err)


@app.route('/')
def hello():
    return Response(render_template('index.html', mimetype='txt/html'))

def allowed_file(filename):
    if filename.rsplit('.', 1)[1].lower() in ['png', 'jpg']:
        return '.' in filename and filename.rsplit('.', 1)[1].lower()
    else:
        return False

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    lista = ('',url)
    download = download_images(lista)
    return Response(render_template('index.html', mimetype='txt/html'))

@app.route('/up', methods=['POST'])
def up():
    name = request.form.get('name')
    try:
        filename = None
        array_img = []      
        
        # check if the post request has the file part
        
       # if request.method == 'POST':
            #print(request.files.getlist("file"))
        file = request.files
        # if 'file' not in request.files:
        #     flash('No file part')
           
        #file = request.files['file']
        salir = len(file)
        print(file)
        for fruta in file:
            print(request.files[fruta])
            file = request.files[fruta]
 

            # if user does not select file, browser also
            # submit an empty part without filename
            
            if file.filename != '':
                if not allowed_file(file.filename):
                    return response(render_template('index.html', mimetype='text/html'))
                if file and allowed_file(file.filename):
                    extracted_format = (file.filename).split('.')

                    new_name = re.sub('[^A-Za-z0-9]+', '', extracted_format[0])

                    filename = secure_filename(new_name + '.' + extracted_format[1])

                    full_path= '/home/coder/Downloads/repository'
                    file.save(os.path.join(full_path, filename))
                    array_img = (full_path, filename)

            _filename = filename 
           
        return Response(render_template('index.html', name = name ,mimetype='txt/html'))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno,e)

if __name__ == '__main__':
    app.run()
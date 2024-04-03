from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
import cv2
from placingNoBG_onTemplates import overlay_rgba_on_rgb
from gpt_api import comp

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "userUploadLOGO"
output_file_name = []

@app.route("/")
def main():
    imgs = os.listdir("static/formatTemplates")
    return render_template("displayImage.html", images=imgs)

@app.route("/logo/<string:file>")
def logoUpload(file):
    return render_template("fileUpload.html", img=f"{file}.PNG", endpoint=file)

@app.route("/logo/<string:templateS>", methods=['GET', 'POST'])
def upload_file(templateS):
    if request.method == 'POST':
        file = request.files['file']
        textarea = request.form.get("textarea")
        print(textarea)
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(upload_path)
            templatePath = "static/formatTemplates"
            MaxToken=300
            result = comp(textarea, MaxToken, outputs=1)[0]
            
            outputFolder = os.path.join("static/generatedTemplates", "output.png")
            output_file_name.append("output.png")
            template = os.path.join(templatePath, f"{templateS}.PNG")
            
            overlay_rgba_on_rgb(upload_path, template, outputFolder, x=50, y=50, text=result)

            return render_template("generating_one_template.html", image="output.png", res=f"Generated string type has max length of {MaxToken}")

@app.route("/show")
def show():
    return render_template("displayImage.html", images=output_file_name)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)

"""
from flask import Flask, render_template, request, url_for, redirect
import os
from placingNoBG_onTemplates import overlay_rgba_on_rgb
from gpt_api import comp

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "userUploadLOGO"
output_file_name = []


@app.route("/")
def main():
    imgs = os.listdir("static/formatTemplates")
    return render_template("displayImage.html", images=imgs)

@app.route("/logo/<string:file>")
def logoUpload(file):
    return render_template("fileUpload.html", img=f"{file}.PNG", endpoint=file)

@app.route("/logo/<string:templateS>", methods=['GET', 'POST'])
def upload_file(templateS):
    if request.method == 'POST':
        file = request.files['file']
        textarea = request.form.get("textarea")
        print(textarea)
        filename = file.filename
        template_name = f"{templateS}.PNG"
        upload_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(upload_path)
        templatePath = "static/formatTemplates"
        MaxToken=300
        result = comp(textarea, MaxToken, outputs=1)[0]
        
        outputFolder = os.path.join("static/generatedTemplates", "output.png")
        output_file_name.append("output.png")
        template = os.path.join(templatePath, template_name)
        overlay_rgba_on_rgb(upload_path, template, outputFolder, x=5, y=5, text=result)

        return render_template("generating_one_template.html", image="output.png", res=f"Generated string type has max length of {MaxToken}")

@app.route("/show")
def show():
    return render_template("displayImage.html", images=output_file_name)



if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
"""

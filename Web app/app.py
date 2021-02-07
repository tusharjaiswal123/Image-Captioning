from flask import Flask, render_template, request
import caption

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods = ['POST'])
def captioning():
    if request.method == 'POST':
        f = request.files['userfile']
        path = './static/{}'.format(f.filename)
        f.save(path)

        cap = caption.caption_this_image(path)
        result_dic = {
            'image':path,
            "caption":cap
        }
    
    return render_template("index.html",your_result = result_dic) 


if __name__ == '__main__':
    app.run(debug=True)
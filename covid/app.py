from flask import Flask,render_template,request
from covidawarenessml import predict
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form['prediction']
        
        context = [
            {
            'name':predict(data)
            }
        ]
        return render_template('result.html',context = context)
    return render_template('index.html')  



if __name__ == '__main__':
    app.run(port  = 5000,debug = True)








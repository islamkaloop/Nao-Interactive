from flask_cors import CORS
from flask import Flask, request, redirect, url_for, render_template
import os
import math
from Nao import generate
import qi
connection_url = "tcp://192.168.43.148:9559"
appl = qi.Application(["--qi-url=" + connection_url])
app = Flask(__name__)
CORS(app, support_credentials=True)
import os.path

@app.route('/')
def output():
    # serve index template
    return "Hello World"

@app.route('/savecode', methods=['POST'])
def savecode():
    data = request.get_json()
    code = str(data['Code'])
    code1=code.split("\n")
    code=""
    Nao=None
    for x in code1:
        if(x == 'Nao=generate("English")'):
            Nao=generate("English",appl)
        elif(x == 'Nao=generate("Arabic")'):
            Nao=generate("Arabic",appl)
        elif(x == "import math" or x =="from Nao import generate"):
            code=code
        else:
            code=code+x+"\n"
    Nao
    exec(code)
    return ''

@app.route('/receiver', methods = ['POST'])
def worker():
# read json + reply
    data = request.get_json()
    result = ''
    print (data,result)



if __name__ == '__main__':
	app.run()




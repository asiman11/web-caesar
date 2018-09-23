from flask import Flask, render_template, request
import caesar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template('results.html')

@app.route('/home/results', methods=['POST'])
def results():
    rot_amount = request.form.get("rotation-amount")
    new_text = request.form.get("blocktext")
    encrypted_msg = caesar.encrypt(new_text, rot_amount)
    #return encrypted_msg 
    ## TODO:
    # run caeser algorithm
    # receive back a list|string| whatever you want with the answer
    return render_template('results.html', enc = encrypted_msg, rot = rot_amount, newtext = new_text)

app.run(debug = True)
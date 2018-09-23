from flask import Flask, render_template, request
import caesar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        rot_amount = int(request.form.get("rotation-amount"))
        new_text = str(request.form.get("blocktext"))
        encrypted_msg = caesar.encrypt(new_text, rot_amount)
        return render_template('results.html', rot_amount=rot_amount, new_text=new_text, encrypted_msg=encrypted_msg)
    return render_template('index.html')
    
app.run(debug = True)
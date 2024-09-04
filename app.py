from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method in ['POST','GET']:
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        
        return redirect(url_for('form', name1=name1, name2=name2))
    return render_template('index.html')
@app.route('/formpage')
def form():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    score = random.randint(1,100)

    values = {
        'friend_one' : name1,
        'friend_two' : name2,
        'scores'     : score
    }
    return render_template('metor.html', item = name1, item2 = name2, score = score)
    

if __name__ == '__main__':
    app.run(debug=True)
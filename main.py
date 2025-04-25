from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# mitose

@app.route('/mitose/interfase')
def mi_interfase():
    return render_template('mi_interfase.html')

@app.route('/mitose/profase')
def mi_profase():
    return render_template('mi_profase.html')

@app.route('/mitose/metafase')
def mi_metafase():
    return render_template('mi_metafase.html')

@app.route('/mitose/anafase')
def mi_anafase():
    return render_template('mi_anafase.html')

@app.route('/mitose/telofase')
def mi_telofase():
    return render_template('mi_telofase.html')

@app.route('/mitose/esquema')
def mi_esquema():
    return render_template('mi_esquema.html')


#meiose 1

@app.route('/meiose/interfase')
def me_interfase():
    return render_template('me_interfase.html')

@app.route('/meiose/profase1')
def me_profase1():
    return render_template('me_profase1.html')

@app.route('/meiose/metafase1')
def me_metafase1():
    return render_template('me_metafase1.html')

@app.route('/meiose/anafase1')
def me_anafase1():
    return render_template('me_anafase1.html')

@app.route('/meiose/telofase1')
def me_telofase1():
    return render_template('me_telofase1.html')

#meiose 2

@app.route('/meiose/profase2')
def me_profase2():
    return render_template('me_profase2.html')

@app.route('/meiose/metafase2')
def me_metafase2():
    return render_template('me_metafase2.html')

@app.route('/meiose/anafase2')
def me_anafase2():
    return render_template('me_anafase2.html')

@app.route('/meiose/telofase2')
def me_telofase2():
    return render_template('me_telofase2.html')

@app.route('/meiose/esquema')
def me_esquema():
    return render_template('me_esquema.html')


if __name__ == '__main__':
    app.run()


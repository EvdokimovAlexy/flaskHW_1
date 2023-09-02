from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {},

    ]
    return render_template('clothes.html', clothes_list=clothes_list)


@app.route('/jackets/')
def jackets():
    jacket_list = [
        {
         },

    ]
    return render_template('jackets.html', jacket_list=jacket_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {
         }
    ]
    return render_template('shoes.html', shoes_list=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)

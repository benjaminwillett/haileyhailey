
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def default():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()




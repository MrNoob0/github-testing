import configparser
from flask import *
from moonraker import moonraker

config = configparser.ConfigParser()

def readConfig(configfile):
    config.read(configfile)
    config.sections()

readConfig('config.ini')

#--------------------------------------------------#
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/home-all/')
def my_link():
  moonraker.sendgcode('G28')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)

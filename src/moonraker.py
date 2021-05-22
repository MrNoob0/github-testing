import requests
import configparser

config = configparser.ConfigParser()

def readConfig(configfile):
    config.read(configfile)
    config.sections()

readConfig('config.ini')

class connectionsettings():
    ip = config['connection']['host']
    port = config['connection']['port']

class moonraker():
    def sendgcode(gcode):
        x = requests.post(f'' + connectionsettings().ip + ':' + connectionsettings().port + '/printer/gcode/script?script=' + gcode)
    def restart(service):
        x = requests.post(f'' + connectionsettings().ip + ':' + connectionsettings().port + '/machine/services/restart?service=' + service)
    def status():
        x = ('192.168.1.70:7125/printer/info')

print (connectionsettings().ip)
print (connectionsettings().port)

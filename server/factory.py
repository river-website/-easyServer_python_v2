from server.webServer import *
from server.baseServer import *

def getServer(serverName=None):
    if serverName == 'webServer':
        return webServer()
    else:
        return baseServer()
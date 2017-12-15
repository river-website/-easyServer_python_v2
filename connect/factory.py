from connect.tcpConnect import *

def getConnect(connectName):
    if connectName == 'tcp':
        return tcpConnect()
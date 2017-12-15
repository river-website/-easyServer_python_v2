from easy import *
from baiduyun.app import *
if __name__ == '__main__':
    baiduyunApp = baiduyun()
    server = {
        'webServer':{
            '0.0.0.0:81':{
                'webSite':baiduyunApp
            },
        }
    }
    easy().start(server)

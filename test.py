from easy import *
if __name__ == '__main__':
    server = {
        'webServer':{
            '0.0.0.0:81':{
                'webSite':'/html/'
            },
            '0.0.0.0:88':{
                'webSite':'/html/'
            }
        }
    }
    easy().start(server)

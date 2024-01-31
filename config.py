import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or b'r]\x99\xcd\xadcCf\xfb\x084\x90+\x0e@\x96'

    MONGODB_SETTINGS={'db':'UTA_Enrollment'}
                      
                      
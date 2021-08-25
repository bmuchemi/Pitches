import os 

class Config:
    '''
    '''
    UPLOADED_PHOTOS_DEST='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bmuchemi:9262@localhost/pitches'

    #email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(Config):
    '''
    '''
    pass

class DevelopmentConfig(Config):
    '''
    '''
    
    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
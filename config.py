import os 

class Config:
    '''
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bmuchemi:BENJA9262@localhost/pitches'

class ProdConfig(Config):
    '''
    '''
    pass

class DevConfig(Config):
    '''
    '''
    DEBUG=True

config_options={
    'development': DevConfig,
    'production': ProdConfig
}

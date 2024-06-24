class Config(object):
    TESTING = True
    ENV="development"

class ProductionConfig(Config):
    ENV="production"
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    TESTING = True
# Configuration settings for the application

import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    API_VERSION = os.getenv('API_VERSION', 'v1')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
    TIMEZONE = os.getenv('TIMEZONE', 'UTC')
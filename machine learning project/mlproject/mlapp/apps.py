from django.apps import AppConfig

from django.conf import settings
import os
import pickle


class MlappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mlapp'

class PredictorConfig(AppConfig):

    # create path to models
    path = os.path.join(settings.MODELS, 'models.p')
 
    # load models into separate variables these will be accessible via this class
    with open(path, 'rb') as pickled:
       data = pickle.load(pickled)
    
    X_test = data['X_test']
    y_test = data['y_test']
    regressor = data['regressor']
    vectorizer = data['vectorizer']
    models = data['models']

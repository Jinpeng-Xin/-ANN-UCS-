from keras.models import load_model

def ann_ucs():
    model = load_model('冻土ucs.h5')
    return model
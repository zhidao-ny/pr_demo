from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import time
import pickle

SEQUENCE_LENGTH = 300

class Predict():
    def __init__(self):
        self.model = load_model("./model.h5")
        self.tokenizer = pickle.load(open('./tokenizer.pkl','rb'))
    def sentiment(self,text):
        # input: string 
        # output: dict
        start_at = time.time()
        x_test = pad_sequences(self.tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
        score = self.model.predict([x_test])[0]
        return {"score": float(score),
           "elapsed_time": time.time()-start_at}
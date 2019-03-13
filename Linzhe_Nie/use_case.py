#!/home/aqz/anaconda2/bin/python
from nlp_predict import Predict

text = "I love the music"
predict = Predict()

print '\n'
print "Result: ",predict.sentiment(text)
print '\n'

# Predict.sentiment method:
# input: string eg: "i love the music"
# output: dict  eg: {'elapsed_time': 0.25691890716552734, 'score': 0.9774266481399536}
# score = 1 means absolutely positive sentiment
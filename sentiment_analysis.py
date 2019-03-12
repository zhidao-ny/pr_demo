from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3

analyzer = SentimentIntensityAnalyzer().polarity_scores

def sentiment(topic,db,table,score_func):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM {table};".format(table="tweets"))
    results = cursor.fetchall()
    i = 0
    neg = 0
    compound = 0
    pos = 0
    neu = 0
    for r in results:
        if topic in r[0]:
            # print(r[0],score_func(r[0]))
            i += 1
            neg += score_func(r[0])["neg"]
            compound += score_func(r[0])["compound"]
            pos += score_func(r[0])["pos"]
            neu += score_func(r[0])["neu"]
    if i > 0:
        return (neg/i), (compound/i), (pos/i), (neu/i)
        print("neg:      %.2f" % (neg/i))
        print("compound: %.2f" % (compound/i))
        print("pos:      %.2f" % (pos/i))
        print("neu:      %.2f" % (neu/i))
    else:
        return null, null, null, null
        print("no record with keyword:", topic)
    #print(i)
    cursor.close()
    connection.close()
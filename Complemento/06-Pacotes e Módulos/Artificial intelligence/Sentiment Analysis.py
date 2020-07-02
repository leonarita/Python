from textblob import TextBlob
# import emoji

y = input("Enter the sentence: ")
edu = TextBlob(y)

x = edu.sentiment.polarity

if x < 0:
    # print("Negative sentence, demotivating", emoji.emojize(":disappointed_face:"))
    print("Negative sentence, demotivating")
elif x == 0:
    # print("Neutral", emoji.emojize(":zipper-mouth_face:"))
    print("Neutral")
elif 0 < x <= 1:
    # print("Positive, joyfull", emoji.emojize(":grinning_face_with_big_eyes:"))
    print("Positive, joyfull")
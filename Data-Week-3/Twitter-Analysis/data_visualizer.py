'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
total_polarity = 0
total_subjectivity = 0
polarityList = []
subjectivityList = []
allTheTweets = ''
for index in range(0,len(tweetData)):#maybe -1
    # Get the text
    text = tweetData[index]['text']
    allTheTweets += text

    textBlob = TextBlob(text)
    # the polarity of the current tweet
    current_polarity = textBlob.polarity
    # add it to the total polarity
    total_polarity += current_polarity
    polarityList.append(current_polarity)

    current_subjectivity = textBlob.subjectivity
    # add it to the total subjectivity
    total_subjectivity += current_subjectivity
    subjectivityList.append(current_subjectivity)

allTextBlobs = TextBlob(allTheTweets)
filtered_words_counts ={}
exclude_words = ['automation', 'http', 'good', 'http', 'potential', 'twitter', 'should', 'intelligent', 'million']
for word in allTextBlobs.words:
    if len(word)<=3 or (len(word)<5 and word != word.upper()) or ('http' in word) :

    if((len(word)>5 and word.lower() not in exclude_words) or word == word.isupper())):
        filtered_words_counts[word] = allTextBlobs.word_counts[word]
wc = WordCloud().generate_from_frequencies(filtered_words_counts)
plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")
plt.show()











# print("Average polarity: ",total_polarity/len(tweetData))
# print("Average subjectivity: ",total_subjectivity/len(tweetData))
# total = total_polarity + total_subjectivity
#
#
# plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -.25, 0, .25, .5, .75, 1.1])
# plt.xlabel("Polarities")
# plt.ylabel("Number of Tweets")
# plt.title("Histogram of Tweet polarity")
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
# plt.show()

# plt.hist(subjectivityList, bins=[0, .25, .5, .75, 1.1])
# plt.xlabel("Subjectivities")
# plt.ylabel("Number of Tweets")
# plt.title("Histogram of Tweet subjectivity")
# plt.axis([0, 1.1, 0, 100])
# plt.grid(True)
# plt.show()
#
# labels = ['Polarity', 'Subjectivity']
# sizes = [total_polarity, total_subjectivity]
# colors = ['lightskyblue', 'lightcoral']
# patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.show()
#
# # Create data
#
#
# colors = (0,0,0)
# area = np.pi*3
#
# # Plot
# plt.scatter(subjectivityList, polarityList, s=area, c=colors, alpha=0.5)
# plt.title('Subjectivity vs polarity scatter plot')
# plt.xlabel('subjectivity')
# plt.ylabel('polarity')
# plt.show()

# Textblob sample:
# tb = TextBlob("I love you and would give you some of the beautiful and magnificent cake but the look on face makes me want to spill your guts; you are amazingly brilliant and i look forward . ")
# print(tb.polarity)

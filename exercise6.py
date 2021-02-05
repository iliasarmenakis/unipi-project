import tweepy

ACCESS_TOKEN =
ACCESS_SECRET =
CONSUMER_KEY =
CONSUMER_SECRET =


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

# getting the words from the given acc 
user = input("user:")
word_list=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)
# spliting the words and sorting them
lekseis=[]
for tweet in word_list:
    spasmeno = tweet.split()
    lekseis = lekseis + spasmeno

def Sorting(lekseis):
    lekseis.sort(key=len)
    return lekseis

print(Sorting(lekseis))
# getting the symbols removed 
SYMBOLS = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

results = []
for element in lekseis:
    temp = ""
    for ch in element:
        if ch not in SYMBOLS:
            temp += ch

    results.append(temp)

# finding the 5 biggest and the 5 shortest words 
for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])

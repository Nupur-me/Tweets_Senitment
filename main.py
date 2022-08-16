from textblob import TextBlob
import tweepy


mykeys = open('twitterkey.txt', 'r').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = input('Enter the Topic you want to get Sentiment Analysis of : ')
tweet_amount = int(input('Enter the amount of Tweets you want to get Sentiment Analysis of : '))

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
neutral = 0
negative = 0

# print('--------------------TWEET-----------------------')

for tweet in tweets:
    final_tweet = tweet.text.replace('RT', '')
    if final_tweet.startswith(' @'):
        position = final_tweet.index(':')
        final_tweet = final_tweet[position+2:]
    if final_tweet.startswith('@'):
        position = final_tweet.index(' ')
        final_tweet = final_tweet[position+2:]
    analysis = TextBlob(final_tweet)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1
    polarity += tweet_polarity
    print(" ")
    print('--------------------Tweets-----------------------')
    print(final_tweet)

print(" ")
print('--------------------POLARITY-----------------------')

print(polarity)
print(f'Amount of Positive Tweets: {positive}')
print(f'Amount of Negative Tweets: {negative}')
print(f'Amount of Neutral Tweets {neutral}')











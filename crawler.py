from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import MySQLdb
import time
import json





#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","rootpass","SM_ANALYZER")

c = conn.cursor()


#consumer key, consumer secret, access token, access secret.

ckey="dZjfrkZ88O2TpQ9Dn2iDz6nCE"
csecret="f1D8wWUjdRqX80BtPhHmhBzUkCFHQYQlDVTByHqRU1BWt5qpC3"
atoken="3961145415-opqGDo1NJOcbX6jZWm7G8R5CzhAHovrAUtm0Pw4"
asecret="ijuqXlfUbkzslJ05Hft0qREtAVW4jrR1V3LSmmG47LnLw"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        print (tweet)
        
        username = all_data["user"]["screen_name"]
        
        c.execute("INSERT INTO entries (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

# print ("Bkp1")
auth = OAuthHandler(ckey, csecret)
# print ("Bkp2")
auth.set_access_token(atoken, asecret)
# print ("Bkp3")

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text


twitterStream = Stream(auth, listener())
# print ("Bkp4")
twitterStream.filter(track=["drug addiction"])
# print ("Bkp5")
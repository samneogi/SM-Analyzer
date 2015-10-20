import tweepy

ckey="dZjfrkZ88O2TpQ9Dn2iDz6nCE"
csecret="f1D8wWUjdRqX80BtPhHmhBzUkCFHQYQlDVTByHqRU1BWt5qpC3"
atoken="3961145415-opqGDo1NJOcbX6jZWm7G8R5CzhAHovrAUtm0Pw4"
asecret="ijuqXlfUbkzslJ05Hft0qREtAVW4jrR1V3LSmmG47LnLw"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
# Importing Modules/Libraries
import tweepy
import time

# Credentials (Insert your keys and tokens below)
api_key = "iE24CaWiw5b6m66MKGMMBKkGe"
api_secret = "qW1TuFX7e9EyhPysCcJVqSwDi0u4BPnzdBK0Eq3cxTAJNyBsoJ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAACHHjAEAAAAA9NMtH9YhGJCrK29rimYyzfiAQBo%2B5Tgvw%3DKghLclShhImb2nZDENkcvurx0QLoHAwYgXoSqPphpS31FuKdfg"
access_token = "1314432660320727042-Rg3d1sbcp3B8Nm6a64nmkISMGrvJwq"
access_token_secret = "fcrMWV1TtEgfLVjhBawq1jq4XdVRGSMYDudSj7zdtXmaU"

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth2UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
client_id = client.get_me().data.id
# Message to reply with if someone mentions the bot
'''message = "Send me a message if you have any questions"

# Bot's unique ID
client_id = client.get_me().data.id
# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    response = client.get_users_mentions(client_id, since_id=start_id)

    # Reply Code
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(5)'''
i = 60
while i > 0:
    api.update_status(i)
    i -= 1
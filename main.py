import tweepy
import picture

bearer_token = r"BAERER_TOKEN" #Just put it for future usage

consumer_key = " YOUR CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"

access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Start
picture.create()

media = api.media_upload("--YOUR RELATIVE PATH--\high_quality_progress_bar.jpg", chunked=True, media_category="tweet_image")
media_ids = [media.media_id]

response = client.create_tweet(
    text = f"{picture.year()} is {picture.num()}% complete.",
    media_ids = media_ids
)
print(f"https://twitter.com/user/status/{response.data['id']}")



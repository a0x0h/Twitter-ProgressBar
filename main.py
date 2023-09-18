import tweepy
import picture

bearer_token = r"AAAAAAAAAAAAAAAAAAAAAI4DqAEAAAAAPi%2BQuLJqPIavagsF2ZIHMkARt%2FE%3DPvAvW8Fat99o9hCdjTva69HcMH054nGDMgl5xQjpPdXJgBRfyi"

consumer_key = "kyirBouSEsBj2RXN1HD0OkJYC"
consumer_secret = "UmnjfdgRkunNrqWiF4YlKyocfc9u83IihZfr1DHDpI3DruFtYd"

access_token = "1703425097007034369-CKwlNKmmTDGLhjUIVb7V7N6ZKDGsTT"
access_token_secret = "GcifmmS263GeyyTf83JZj7DskKiNaCpVw5i8MbgQqoWGV"

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

media = api.media_upload("..\Twitter API\high_quality_progress_bar.jpg", chunked=True, media_category="tweet_image")
media_ids = [media.media_id]

response = client.create_tweet(
    text = f"{picture.year()} is {picture.num()}% complete.",
    media_ids = media_ids
)
print(f"https://twitter.com/user/status/{response.data['id']}")



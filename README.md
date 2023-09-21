# Twitter Progress Bar 2023  <img src="https://pbs.twimg.com/profile_images/1683899100922511378/5lY42eHs_bigger.jpg" data-canonical-src="https://pbs.twimg.com/profile_images/1683899100922511378/5lY42eHs_bigger.jpg" width="40" height="40" />

Twitter Automation to set a progress bar in the **Persian** calendar. _**(Upload Media and Authentication Fixed🛠)**_

- **#1 Pillow Library to generate images:**

![image](https://github.com/aboldeveloper/Twitter-ProgressBar/assets/55990386/b8468d63-b4d7-41bc-8b1c-cf2d5f01ca9d)

- **#2 Run Linux server to run Python script automatically:**

  More Information is in Linux-info.txt

- **#3 Twitter API (IMPORTANT):**

  V2/V1 -> Auth, Post:
  - Just put your API/Consumer, access key and secret in the main.py
  - We need both v2 & v1 API to Authenticate.
  
  V1 (limitation) -> Upload Media (Photo):
  - Media Id Should be list
        
        media = api.media_upload("PATH\image.jpg", chunked=True, media_category="tweet_image")
        media_ids = [media.media_id]

  - Response and Post Tweet [Post and manage tweet](https://docs.tweepy.org/en/stable/client.html#tweepy.Client.create_tweet) :

        response = client.create_tweet(
            text = "text",
            media_ids = media_ids
        )

  
  # Relative link
  - [Twitter API Dashboard](https://developer.twitter.com/en/portal/dashboard)
  - [Tweepy Library Doc](https://docs.tweepy.org/en/stable/)
  



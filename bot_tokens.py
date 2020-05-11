from boto.s3.connection import S3Connection
import os

discord_bot_token = S3Connection(os.environ['client_key'], os.environ['S3_SECRET'])
google_api_key = S3Connection(os.environ['google_api'], os.environ['S3_SECRET'])
google_cse_key = S3Connection(os.environ['google_cse'], os.environ['S3_SECRET'])
weather_api_key = S3Connection(os.environ['weather_api'], os.environ['S3_SECRET'])

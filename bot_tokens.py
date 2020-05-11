from boto.s3.connection import S3Connection
import os

discord_bot_token = S3Connection(os.environ['client_key'])
google_api_key = S3Connection(os.environ['google_api'])
google_cse_key = S3Connection(os.environ['google_cse'])
weather_api_key = S3Connection(os.environ['weather_api'])

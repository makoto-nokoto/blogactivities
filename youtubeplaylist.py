#!/usr/bin/python

import httplib2
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
DJANGO_SETTINGS_MODULE = 'activity.settings'
import django
django.setup()

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from activity.models import Post
from django.contrib.auth.models import User


CLIENT_SECRETS_FILE = "client_secret_81048480837-ff1fvgds5j7o0ebbro9r0b6h10bsktkq.apps.googleusercontent.com.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE ="dmi" """
WARNING: Please configure OAuth 2.0

"""
#% os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                   CLIENT_SECRETS_FILE))

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  message=MISSING_CLIENT_SECRETS_MESSAGE,
  scope=YOUTUBE_READONLY_SCOPE)

storage = Storage("%s-oauth2.json" % sys.argv[0])
credentials = storage.get()

if credentials is None or credentials.invalid:
  flags = argparser.parse_args()
  credentials = run_flow(flow, storage, flags)

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  http=credentials.authorize(httplib2.Http()))

# Retrieve the contentDetails part of the channel resource for the
# authenticated user's channel.
channels_response = youtube.channels().list(
  mine=True,
  part="contentDetails"
).execute()

for channel in channels_response["items"]:
  # From the API response, extract the playlist ID that identifies the list
  # of videos uploaded to the authenticated user's channel.
  uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["likes"]

  print("Videos in list %s" % uploads_list_id)

  # Retrieve the list of videos uploaded to the authenticated user's channel.
  playlistitems_list_request = youtube.playlistItems().list(
    playlistId=uploads_list_id,
    part="snippet",
    maxResults=5
  )
  i=0
  for post in Post.objects.all():
      post.delete()

  me = User.objects.get(username='919im')

  while playlistitems_list_request:
    playlistitems_list_response = playlistitems_list_request.execute()

    # Print information about each video.
    for playlist_item in playlistitems_list_response["items"]:
      i=1+i
      video_title = playlist_item["snippet"]["title"]
      video_id = playlist_item["snippet"]["resourceId"]["videoId"]
      video_url="https://www.youtube.com/watch?v="+video_id
      print("%s:%s (%s)" % (i,video_title, video_url))
      Post.objects.create(author=me,title=video_title,url=video_url,text=i).publish()
      if i>4:
          break
    playlistitems_list_request = youtube.playlistItems().list_next(
      playlistitems_list_request, playlistitems_list_response)
    if i>4:
        break

  print

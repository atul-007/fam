import datetime

import requests
import json

from .constants import YOUTUBE_API_URL, SEARCH_STRING_FOR_VIDEO, MAX_RESULTS_PER_API_CALL
from .models import APIAuthKey
from .service import YoutubeService
from .utils import get_date_time_n_secs_ago
from fampay import celery_app


@celery_app.task
def fetch_videos():
    """
        This function fetch the videos from Youtube
    """
    print("Running fetching video task ", datetime.datetime.now())

    # Setting published_after to 1 hour ago time from current time
    published_after = get_date_time_n_secs_ago(3600)
    print("publishAfterTime", published_after)

    # Getting valid Auth key from DB
    auth_key = APIAuthKey.get_auth_key()
    if not auth_key:
        print("Please add API Auth Key. No auth key available")
        return
    videos = []
    print(auth_key)
    try:
        # Calling Youtube search api to get the videos
        response = requests.get(YOUTUBE_API_URL, params={
            'part': 'snippet',
            'maxResults': MAX_RESULTS_PER_API_CALL,
            'q': SEARCH_STRING_FOR_VIDEO,
            'key': auth_key,
            'publishedAfter': published_after,
        })
        data = json.loads(response.text)
        videos = data.get('items', [])
        print (videos)
    except Exception as e:
        # Considering this exception because api key may got exhausted,
        # marking auth key as exhausted
        APIAuthKey.mark_auth_key_exhausted(auth_key)
        print("There is error while making request to youtube. May be authKey get exhausted. Error: ", e)

    # save videos in the database
    YoutubeService.process_videos(videos)

@celery_app.task
def sample_task():
    print("sample task running")

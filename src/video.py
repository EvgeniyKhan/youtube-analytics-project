import os

from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Video:
    def __init__(self, video_id):
        try:
            self.video_id = video_id
            video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                              id=self.video_id).execute()
            self.title = video_response['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={self.video_id}"
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
            self.duration = video_response['items'][0]['contentDetails']['duration']
        except Exception as error:
            self.error = error
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None
            self.duration = None

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_service(cls):
        api_key = os.getenv("YT_API_KEY")
        cls.youtube = build('youtube', 'v3', developerKey=api_key)
        return build('youtube', 'v3', developerKey=api_key)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{self.title}"

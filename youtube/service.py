from youtube.models import Video
import logging

logger = logging.getLogger(__name__)

class YoutubeService:
    """
    This class contains business logic or computation if any
    required for the YouTube service.
    """

    @classmethod
    def process_videos(cls, videos: list):
        """
        Save video data to the database.

        Args:
            videos (list): List of video data dictionaries.

        Returns:
            None
        """
        if not videos:
            logger.warning("No videos fetched from YouTube search API")
            return

        for video in videos:
            try:
                Video.objects.create(
                    title=video['snippet']['title'],
                    description=video['snippet']['description'],
                    publish_datetime=video['snippet']['publishedAt'],
                    video_id=video['id']['videoId'],
                    channel_id=video['snippet']['channelId'],
                    thumbnail_url=video['snippet']['thumbnails']['default']['url']
                )
                logger.info("Video saved successfully: %s", video['id']['videoId'])
            except KeyError as ke:
                logger.error("KeyError while saving video to database: %s", str(ke))
            except Exception as e:
                logger.error("Error while saving video to database: %s", str(e))

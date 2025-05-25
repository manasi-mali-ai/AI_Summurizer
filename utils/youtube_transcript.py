from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_youtube_transcript(url):
    video_id = re.search(r"(?:v=|be/)([a-zA-Z0-9_-]{11})", url).group(1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript])

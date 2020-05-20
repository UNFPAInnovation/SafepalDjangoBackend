import ffmpeg_streaming
from django.db.models.signals import post_save

from .models import Video
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from ffmpeg_streaming import FFProbe
import time


def convert_video_and_extract_meta_data(sender, **kwargs):
    """
    Converts the uploaded video into 480 mp4 files that can be streamed using the .m38u file.
    The duration of the files is then extracted from the file and resaved in the Video object
    """
    instance = kwargs['instance']
    video_path = instance.url.path

    if instance.url.storage.exists(instance.url.name):
        video = ffmpeg_streaming.input(video_path)
        hls = video.hls(Formats.h264())
        _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
        hls.representations(_480p)
        hls.output()

        duration_in_seconds = int(float(FFProbe(instance.url.path).streams().video().get('duration', 60)))
        minutes = int(time.strftime('%M', time.gmtime(duration_in_seconds)))
        Video.objects.filter(pk=instance.pk).update(duration=minutes if minutes > 1 else 1)


post_save.connect(convert_video_and_extract_meta_data, sender=Video)
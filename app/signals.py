import ffmpeg_streaming
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Video
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from ffmpeg_streaming import FFProbe
import time


@receiver(post_save, sender=Video)
def convert_video_and_extract_meta_data(sender, instance, **kwargs):
    """
    Converts the uploaded video into 480 mp4 files that can be streamed using the .m38u file.
    The duration of the files is then extracted from the file and resaved in the Video object
    """
    video = ffmpeg_streaming.input(instance.url.path)
    hls = video.hls(Formats.h264())
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    hls.representations(_480p)
    hls.output()

    duration_in_seconds = int(float(FFProbe(instance.url.path).streams().video().get('duration', 60)))
    minutes = int(time.strftime('%M', time.gmtime(duration_in_seconds)))
    instance.duration = minutes if minutes > 1 else 1
    instance.save(update_fields=['duration'])

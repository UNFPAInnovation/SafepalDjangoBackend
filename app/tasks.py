from celery import shared_task
import ffmpeg_streaming
from .models import Video
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from ffmpeg_streaming import FFProbe
import time


@shared_task
def async_convert_video_and_extract_meta_data(id):
    """
    Converts the uploaded video into 480 mp4 files that can be streamed using the .m38u file.
    The duration of the files is then extracted from the file and resaved in the Video object
    """
    print('async convert video running')
    print(id)
    instance = Video.objects.get(id=id)
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
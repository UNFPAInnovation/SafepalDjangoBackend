from django.db.models.signals import post_save
from app.tasks import async_convert_video_and_extract_meta_data
from .models import Video


def post_save_video_receiver(sender, **kwargs):
    instance = kwargs['instance']
    async_convert_video_and_extract_meta_data.delay(instance.id)

post_save.connect(post_save_video_receiver, sender=Video)
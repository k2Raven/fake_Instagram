from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from webapp.models import Publication

@receiver(post_save, sender=Publication)
def create_publication(sender, instance, created, **kwargs):
    if created:
        author = instance.author
        author.count_publications += 1
        author.save()

@receiver(post_delete, sender=Publication)
def delete_publication(sender, instance, **kwargs):
    author = instance.author
    author.count_publications -= 1
    author.save()

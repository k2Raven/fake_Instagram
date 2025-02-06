from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from webapp.models import Publication, Comment


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


@receiver(post_save, sender=Comment)
def create_comment(sender, instance, created, **kwargs):
    if created:
        publication = instance.publication
        publication.comments_counter += 1
        publication.save()


@receiver(post_delete, sender=Comment)
def delete_comment(sender, instance, **kwargs):
    publication = instance.publication
    publication.comments_counter -= 1
    publication.save()

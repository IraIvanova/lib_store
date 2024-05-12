# from django.contrib.auth.models import User
# from user_vocabulary.models import UserVocabulary
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from datetime import date
#
# @receiver(pre_save, sender=UserVocabulary)
# def create_profile(sender, instance, created, **kwargs):
#     today = date.today()
#     if UserVocabulary.objects.filter(created_at__date=today).count() > 5 and request.user.groups.first.name != "premium_sub":
#         raise ValueError('Bid must be higher than current price')
#
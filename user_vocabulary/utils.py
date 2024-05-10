from .models import UserVocabulary


def find_word_by_id(word_id, user):
    try:
        return UserVocabulary.objects.get(external_id=word_id, user=user, language=user.learned_language)
    except UserVocabulary.DoesNotExist:
        return None

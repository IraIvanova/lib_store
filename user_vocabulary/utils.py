from .models import UserVocabulary


def find_word_by_id(id, user):
    return UserVocabulary.objects.get(external_id=id, user=user, language=user.learned_language)

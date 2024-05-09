from django import template

register = template.Library()


@register.simple_tag()
def get_translation(word, language):
    print(word)
    for t in word['translations']:
        if 'language' in t and t['language'] == language:
            return t['translation']

    return word['word']



from django import template
import re

register = template.Library()


@register.filter
def replace_word(initial_string, replace_word):
    compiled = re.compile(re.escape(replace_word), re.IGNORECASE)
    return compiled.sub(f"<span class='bg-info'>{replace_word}</span>", initial_string)

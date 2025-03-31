from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Post)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Comment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('text',)
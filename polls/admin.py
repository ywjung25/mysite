from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
            ('bomzip question',  {'fields': ['question_text']}),
            (None, {'fields': ['pub_date']}),
        ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text', 'pub_date']
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(Question, QuestionAdmin)

from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['question_level']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently','question_level')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [ 
        (None,              {'fields': ['choice_text']}),
        (None,              {'fields': ['correct_answer']}),
        ('Selection',       {'fields': ['selection'], 'classes': ['collapse']})
    ]
    list_display = ('choice_text', 'selection', 'correct_answer')
    search_fields = ['choice_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

#https://www.mathopolis.com/questions/quizzes.php
#Q lvl1 5 weeks
#Q lvl2 (5 × 4) × (7 − 0)
#Q lvl3 About $30
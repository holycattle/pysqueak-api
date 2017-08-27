from django.contrib import admin

from .models import Question, Choice, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        # put all other fields you want to be shown in listing
        'version', 'title', 'created_on', 'updated_on',
    )

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        # put all other fields you want to be shown in listing
        'text', 'version',
    )
    raw_id_fields = ('question',)
    def version(self, obj):
        return obj.question.version


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        # put all other fields you want to be shown in listing
        'user_id', 'choice_value', 'version',
    )
    raw_id_fields = ('question', 'choice',)
    def version(self, obj):
        return obj.question.version
    def choice_value(self, obj):
        return obj.choice.text


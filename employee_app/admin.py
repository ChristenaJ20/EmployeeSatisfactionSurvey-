from django.contrib import admin
from .models import SurveySubmission

# Register your models here.

@admin.register(SurveySubmission)
class SurveySubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'department', 'rating', 'anonymous', 'submitted_at')
    list_filter = ('department', 'rating', 'anonymous', 'submitted_at')
    search_fields = ('username', 'department', 'comment')
    readonly_fields = ('submitted_at',)

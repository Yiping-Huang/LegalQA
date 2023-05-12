from django.contrib import admin

# Register your models here.
from legal_qa.models import Topic, Description, Reply, Comment

admin.site.register(Topic)
admin.site.register(Description)
admin.site.register(Reply)
admin.site.register(Comment)

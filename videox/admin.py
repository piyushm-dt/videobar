from django.contrib import admin
from videox.models import Video, Comment
# Register your models here.

admin.site.register([Video, Comment])
from django.contrib import admin

from posts.models import Post
from threads.models import Thread


class PostInlineAdmin(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    inlines = [
        PostInlineAdmin,
    ]

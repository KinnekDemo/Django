from django.contrib import admin

# Register your models here.
from fix_it.models import Post, Tag, Annotate


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Annotate)
class AnnotateAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
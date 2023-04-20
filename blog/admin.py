from django.contrib import admin
from blog.models import Post, Category

# Register your models here. Using default configuration so no need for any attributes
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

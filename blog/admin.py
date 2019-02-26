from django.contrib import admin
from .models import Post
#Para tornar nosso modelo visível na página de administração,
# precisamos registrá-lo com admin.site.register(Post)

admin.site.register(Post)


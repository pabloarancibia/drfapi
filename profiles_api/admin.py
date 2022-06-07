from django.contrib import admin

from profiles_api import models

# damos acceso al admin para que edite user profile
admin.site.register(models.UserProfile)

admin.site.register(models.ProfileFeedItem)
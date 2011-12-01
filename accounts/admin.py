# Author: David Guerrero
# Licenced under the terms of the AGPLv3. See LICENCE file for more information.

from accounts.models import UserProfile
from django.contrib import admin

admin.site.register(UserProfile)

# Copyright (C) 2011 David Guerrero
# This file is distributed under the license terms of the LICENSE file.
# David Guerrero <dguerrer@polytch.unice.fr>, 2011.

from accounts.models import UserProfile
from django.contrib import admin

admin.site.register(UserProfile)

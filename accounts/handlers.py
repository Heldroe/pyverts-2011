# Copyright (C) 2011 David Guerrero
# This file is distributed under the license terms of the LICENSE file.
# David Guerrero <dguerrer@polytch.unice.fr>, 2011.

from django.utils.translation import ugettext, ugettext_lazy as _

from avatar.views import _get_avatars

class UploadAvatarAchievement(object):
    name = ugettext("Avatar Uploader")
    key = "avatar_upload"
    description = ugettext("Upload your first avatar")
    bonus = 10.0
    def evaluate(self, user, *args, **kwargs):
        avatars = _get_avatars(user)
        if len(avatars) > 0:
            return True
        else:
            return False

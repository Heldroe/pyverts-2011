# Author: David Guerrero
# Licenced under the terms of the AGPLv3. See LICENCE file for more information.

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

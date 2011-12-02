# Copyright (C) 2011 David Guerrero
# This file is distributed under the license terms of the LICENSE file.
# David Guerrero <dguerrer@polytch.unice.fr>, 2011.

from django.utils.translation import ugettext, ugettext_lazy as _

from avatar.views import _get_avatars
from allauth.socialaccount.models import SocialAccount
from interests.utils import sync_user_fb_interests

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

class FacebookLoginAchievement(object):
    name = ugettext("Facebooker")
    key = "facebook_login"
    description = ugettext("Login with Facebook")
    bonus = 50.0
    def evaluate(self, user, *args, **kwargs):
        try:
            socialaccounts = SocialAccount.objects.get(user=user)
            if socialaccounts.is_fb_account():
                sync_user_fb_interests(user)
            return socialaccounts.is_fb_account()
        except SocialAccount.DoesNotExist:
            return False

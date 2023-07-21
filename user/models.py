# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser,Group, Permission
# from django.utils.translation import gettext as _
# from rest_framework_simplejwt.tokens import RefreshToken

# class CustomUser(AbstractUser):
#     # Your custom fields and additional modifications
#     email = models.EmailField(unique=True)

#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_('The groups this user belongs to.'),
#         related_name='customuser_set'  # Add a related_name argument
#     )

#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name='customuser_set'  # Add a related_name argument
#     )

#     def tokens(self):
#         refresh = RefreshToken.for_user(self)

#         return {
#             'refresh':str(refresh),
#             'access':str(refresh.access_token)
#         }
    
    
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,  **extra_feilds):
        user = self.model(**extra_feilds)
        user.save()
        return user




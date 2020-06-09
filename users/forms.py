from  django_registration.forms import RegistrationForm
from .models import BlogUser


class BlogUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = BlogUser


from django.forms import ModelForm
from matching.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['upload_image']

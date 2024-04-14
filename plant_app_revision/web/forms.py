from django import forms

from plant_app_revision.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Plant.objects.all().delete()
        else:
            return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantEditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantDeleteForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _,field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

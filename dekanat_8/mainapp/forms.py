from django import forms

from mainapp.models import Group, Student


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
            'specialty',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control mt-1'
            item.widget.attrs['style'] = 'resize: none'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'group',
            'surname',
            'name',
            'dob',
            'patronymic',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control mt-1'
            item.widget.attrs['style'] = 'resize: none'

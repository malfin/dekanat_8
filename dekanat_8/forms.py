from django import forms

from mainapp.models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'name',
            'desc',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control mt-1'
            item.widget.attrs['style'] = 'resize: none'
            item.help_text = ''
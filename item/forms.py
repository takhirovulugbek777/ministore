from django import forms

from item.models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'descriptions', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descriptions': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'descriptions', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'descriptions': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

        }

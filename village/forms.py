from django import forms


class ComplaintForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'आपले पूर्ण नाव',
        })
    )
    mobile = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '10 अंकी मोबाइल नंबर',
            'type': 'tel',
            'inputmode': 'numeric',
            'pattern': '[0-9]{10}',
        })
    )
    category = forms.ChoiceField(
        choices=[
            ('', 'प्रकार निवडा'),
            ('water', 'पाणी समस्या'),
            ('road', 'रस्ता समस्या'),
            ('electricity', 'वीज समस्या'),
            ('cleanliness', 'स्वच्छता'),
            ('other', 'इतर'),
        ],
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'rows': 5,
            'placeholder': 'तक्रारीची सविस्तर माहिती लिहा...',
        })
    )

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError('कृपया 10 अंकी मोबाइल नंबर भरा.')
        return mobile

    def clean_category(self):
        category = self.cleaned_data['category']
        if not category:
            raise forms.ValidationError('तक्रारीचा प्रकार निवडा.')
        return category


class ComplaintTrackForm(forms.Form):
    complaint_id = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'उदा. A1B2C3D4E5F6',
            'autocomplete': 'off',
        })
    )
    mobile = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '10 अंकी मोबाइल नंबर',
            'type': 'tel',
            'inputmode': 'numeric',
            'pattern': '[0-9]{10}',
        })
    )

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError('कृपया 10 अंकी मोबाइल नंबर भरा.')
        return mobile

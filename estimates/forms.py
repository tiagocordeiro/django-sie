from django import forms


class EstimateFormAdmin(forms.ModelForm):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('sent', 'Sent'),
        ('accept', 'Accept'),
        ('declined', 'Declined'),
        ('invoiced', 'Invoiced'),
        ('revised', 'Revised'),
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES)

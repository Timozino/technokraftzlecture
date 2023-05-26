# from crispy_forms.helper import FormHelper
# from django import forms
# from courses.models import Course
# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


# class CourseEnrollForm(forms.Form):
#     course = forms.ModelChoiceField(
#         queryset=Course.objects.all(),
#         widget=forms.HiddenInput
#     )


from django import forms
from courses.models import Course


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput
    )

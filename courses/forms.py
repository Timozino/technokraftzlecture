# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Submit
# from django import forms
# from django.forms.models import inlineformset_factory
# from .models import Course, Module
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Submit






# ModuleFormSet = inlineformset_factory(
#     Course,
#     Module,
#     fields=['title', 'description'],
#     extra=2,
#     can_delete=True
# )


# formset_helper = FormHelper()
# formset_helper.form_method = 'post'
# formset_helper.layout = Layout(
#     Fieldset(
#         'Module Information',
#         'title',
#         'description',
#         css_class='module-fieldset'
#     ),
#     Submit('submit', 'Save')
# )

from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

ModuleFormSet = inlineformset_factory(
    Course,
    Module,
    fields=['title', 'description'],
    extra=2,
    can_delete=True
)

formset_helper = None

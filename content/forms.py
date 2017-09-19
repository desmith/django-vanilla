from django import forms
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode

from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


""" Crispy Version """
class FeedbackForm(forms.Form):
  sender = forms.EmailField(label='Sender Email', required=True)
  subject = forms.CharField(max_length=100)
  message = forms.CharField(widget=forms.Textarea)

  def __init__(self, *args, **kwargs):
    super(FeedbackForm, self).__init__(*args, **kwargs)

    self.helper = FormHelper()
    self.helper.form_id = 'feedback'
    self.helper.form_class = 'blueForms'
    self.helper.form_method = 'post'
    self.helper.form_action = '.'
    self.helper.label_class = 'col-4 text-right col-form-label'
    self.helper.field_class = 'col-8'
    self.helper.help_text_inline = True

    self.helper.layout = Layout(
      InlineField('sender'),
      InlineField('subject'),
      InlineField('message'),
    )


    self.helper.add_input(Submit('submit', 'Submit'))


class QuickSearchForm(forms.Form):
  gender = forms.CharField(max_length=100)


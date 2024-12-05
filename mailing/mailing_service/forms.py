from django import forms
from datetimepicker.widgets import DateTimePicker

from .models import RecipientMailing, Message, Mailing


class RecipientMailingForm(forms.ModelForm):
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 400px"}))
    full_name = forms.CharField(label="ФИО",
                                widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}))
    comment = forms.CharField(label="Комментарий",
                              widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}))

    class Meta:
        model = RecipientMailing
        fields = ["email", "full_name", "comment"]


class MessageForm(forms.ModelForm):
    topic_message = forms.CharField(label="Тема письма",
                                    widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}))
    message = forms.CharField(label="Содержание письма",
                              widget=forms.Textarea(attrs={"class": "form-control", "style": "width: 400px"}))

    class Meta:
        model = Message
        fields = ["topic_message", "message"]


class MailingForm(forms.ModelForm):
    start_mailing = forms.DateTimeField(label="Время начала рассылки", input_formats=['%d/%m/%Y %H:%M'],
                                        widget=forms.DateTimeInput(
                                            format='%d/%m/%Y %H:%M',
                                            attrs={'class': 'form-control', 'type': 'datetime-local'}))
    end_mailing = forms.DateTimeField(label="Время окончания рассылки", input_formats=['%d/%m/%Y %H:%M'],
                                      widget=forms.DateTimeInput(
                                          format='%d/%m/%Y %H:%M',
                                          attrs={'class': 'form-control', 'type': 'datetime-local'}))
    messages = forms.ModelChoiceField(
        label="Письмо",
        queryset=Message.objects.all(),
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"}),
    )
    recipients = forms.ModelMultipleChoiceField(label="Получатели",
                                                queryset=RecipientMailing.objects.all(),
                                                widget=forms.SelectMultiple(
                                                    attrs={"class": "form-select"}))

    class Meta:
        model = Mailing
        fields = ["start_mailing", "end_mailing", "messages", "recipients"]

# class FormForCreate(forms.ModelForm):
#     name = forms.CharField(
#         label="Наименование",
#         validators=[validate_words],
#         widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}),
#     )
#     description = forms.CharField(
#         label="Описание",
#         validators=[validate_words],
#         widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 100px"}),
#     )
#     image = forms.ImageField(
#         label="Изображение",
#         validators=[FileExtensionValidator(["jpeg", "png"], "Изображение может быть формата: 'jpeg', 'png'")],
#         widget=forms.FileInput(attrs={"class": "form-control"}),
#     )
#     category = forms.ModelChoiceField(
#         label="Категория",
#         queryset=Category.objects.all(),
#         widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"}),
#     )
#     price = forms.DecimalField(
#         label="Цена", widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 200px"})
#     )
#     is_active = forms.BooleanField(label="Активность", required=False)

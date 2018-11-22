from django import forms
from django.core.validators import RegexValidator

from forms1.models import User


class UserForm(forms.Form):
    # label='用户名'  <label >用户名<label>
    name = forms.CharField(label='用户名', required=True, min_length=6, max_length=12,
                           error_messages={'required': u'用户名必须填写',
                                           'min_length': u'最小长度不能小于6位',
                                           'max_length': u'该字段最大长度不能超过12位',
                                           },
                           )
    password = forms.CharField(label='用户名', widget=forms.PasswordInput)

    #  重写校验方式 全局校验
    def clean(self):
        pass

    #  单个字段校验重写
    def clean_name(self):
        pass


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        # 表示所有字段全部生产html元素
        # fields = '__all__'
        # 指定特定字段生成元素
        fields = ('name', 'password')

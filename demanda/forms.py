from django import forms
from .models import Demanda, Servico, Usuario, Urgencia
from django.contrib.auth.forms import UserCreationForm
from django import template
#from .models import Imagem



#form Demanda

# class DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao' ,'imagem']  # Não inclui 'realizador' e 'realizadoem'
#         widgets = {
#             'titulo': forms.TextInput(),
#             'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
#             'imagem': forms.FileInput(), 
#         }


# class DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao', 'imagem', 'servico', 'urgencia']
#         widgets = {
#             'titulo': forms.TextInput(attrs={'placeholder': 'Digite o assunto'}),
#             'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'placeholder': 'Digite a descrição'}),
#             'imagem': forms.FileInput(),
#         }

#     servico = forms.ModelChoiceField(queryset=Servico.objects.all())
#     urgencia = forms.ModelChoiceField(queryset=Urgencia.objects.all())









class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'cpf', 'perfil', 'area']  # Não precisa adicionar os campos de senha aqui

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Utilize 'password1' ao invés de 'password'
        if commit:
            user.save()
        return user


register = template.Library()
@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class + (" is-invalid" if field.errors else "")})




# class ImagemForm(forms.ModelForm):
#     class Meta:
#         model = Imagem  # Certifique-se de substituir isso pelo seu modelo real
#         fields = ['imagem']
#         widgets = {
#             'imagem': forms.FileInput(attrs={'multiple': True}),
#         }





# # Formulário para cadastrar uma demanda
# class Nova_DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao', 'imagem', 'urgencia', 'servico']  # Campos a serem exibidos no formulário

#         # Personalizando widgets (elementos de formulário HTML)
#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
#             'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
#             'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'urgencia': forms.Select(attrs={'class': 'form-control'}),
#             'servico': forms.Select(attrs={'class': 'form-control'}),
#         }


# class Nova_DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao', 'imagem', 'urgencia', 'servico']  # Campos a serem exibidos no formulário

#         # Personalizando widgets (elementos de formulário HTML)
#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
#             'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
#             'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'urgencia': forms.Select(attrs={'class': 'form-control'}),  # Urgência widget
#             'servico': forms.Select(attrs={'class': 'form-control'}),  # Serviço widget
#         }

#     # Adicionar valor padrão no select de 'urgência'
#     URGENCIA_CHOICES = [('', 'Selecione a prioridade')] + list(Demanda.URGENCIA_CHOICES)  # Adiciona a opção padrão

#     urgencia = forms.ChoiceField(
#         choices=URGENCIA_CHOICES,  # Opções com 'Selecione a prioridade'
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

#     # Adicionar valor padrão no select de 'serviço'
#     servico = forms.ModelChoiceField(
#         queryset=Servico.objects.all(),  # Queryset dos serviços disponíveis no banco de dados
#         empty_label="Selecione um serviço",  # Exibe 'Selecione um serviço' como valor padrão
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )



# class Nova_DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao', 'imagem', 'urgencia', 'servico']

#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
#             'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
#             'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'urgencia': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione uma prioridade'}),
#             'servico': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um serviço'}),
#         }


# class Nova_DemandaForm(forms.ModelForm):
#     class Meta:
#         model = Demanda
#         fields = ['titulo', 'descricao', 'imagem', 'urgencia', 'servico']

#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
#             'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
#             'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

#     # Forçando a criação de campos 'urgencia' e 'servico' para garantir que eles carreguem as opções corretamente
#     urgencia = forms.ModelChoiceField(
#         queryset=Urgencia.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         empty_label="Selecione a Prioridade "  # Exibe um texto padrão quando não há opção selecionada
#     )
    
#     servico = forms.ModelChoiceField(
#         queryset=Servico.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         empty_label="Selecione um Serviço"  # Exibe um texto padrão quando não há opção selecionada
#     )



class Nova_DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['titulo', 'descricao', 'imagem', 'urgencia', 'servico']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    # Definindo urgencia e servico como obrigatórios
    urgencia = forms.ModelChoiceField(
        queryset=Urgencia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecione a Prioridade",
        required=True,
        error_messages={'required': 'Por favor, selecione uma prioridade.'}  # Mensagem de erro personalizada
    )
    
    servico = forms.ModelChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecione um Serviço",
        required=True,
        error_messages={'required': 'Por favor, selecione um serviço.'}  # Mensagem de erro personalizada
    )

    # Definindo 'titulo' e 'descricao' como obrigatórios
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da demanda'}),
        error_messages={'required': 'O título é obrigatório.'}  # Mensagem de erro personalizada
    )

    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        error_messages={'required': 'A descrição é obrigatória.'}  # Mensagem de erro personalizada
    )

    # Campo 'imagem' não é obrigatório
    imagem = forms.ImageField(
        required=False,  # Torna o campo não obrigatório
    )
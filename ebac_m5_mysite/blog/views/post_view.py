# from django.http import HttpResponse
# from django.views import generic


# class PostView(generic.View):
    
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello World')

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class PostView(View):
    def post(self, request):
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')

        # Validação simples
        if not nome or not email:
            return JsonResponse({'erro': 'Dados inválidos'}, status=400)

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'erro': 'Email inválido'}, status=400)

        return HttpResponse('Obrigado por enviar seus dados!')

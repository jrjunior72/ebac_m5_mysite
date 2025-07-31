from django.http import HttpResponse
from django.views import generic

from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# from django.views import View
# from django.http import HttpResponse, JsonResponse
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


# class PostView(View):
#     def post(self, request):
#         nome = request.POST.get("nome", "")
#         email = request.POST.get("email", "")

#         # Validação simples
#         if not nome or not email:
#             return JsonResponse({"erro": "Dados inválidos"}, status=400)

#         try:
#             validate_email(email)
#         except ValidationError:
#             return JsonResponse({"erro": "Email inválido"}, status=400)

#         return HttpResponse("Obrigado por enviar seus dados!")

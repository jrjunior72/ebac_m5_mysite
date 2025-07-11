# import pytest

from django.test import TestCase, Client
from django.urls import reverse


# @pytest.mark.django_db
# def test_post_view(client):
#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.content == b'Hello World'


class TestPostView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("home")  # Nome da URL que você definiu no urls.py

    def test_post_valido(self):
        dados = {"nome": "Ricardo", "email": "ricardo@exemplo.com"}
        resposta = self.client.post(self.url, dados)

        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"Obrigado", resposta.content)

    def test_post_invalido(self):
        dados = {"nome": "", "email": "email-invalido"}
        resposta = self.client.post(self.url, dados)

        self.assertEqual(resposta.status_code, 400)

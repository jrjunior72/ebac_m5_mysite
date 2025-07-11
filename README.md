# 🧩 Módulo 7 – Exercício Prático | Projeto Django EBAC

Este projeto foi desenvolvido como solução para o exercício prático do Módulo 7 do curso de Django da EBAC. O foco da atividade foi aplicar a criação, configuração e teste de um modelo personalizado em Django.

---

## 🚀 Objetivo da tarefa

- Criar um modelo Django próprio
- Registrar o modelo no admin
- Aplicar migrações
- Testar o modelo manualmente via shell
- Criar testes automatizados com `TestCase`
- Implementar factories com `Factory Boy`
- Executar testes com `Pytest`

---

## 🧱 1. Criação do Modelo `Project`

📄 Arquivo: `blog/models/project.py`

```python
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```
📎 Registrado em blog/models/__init__.py:

```python
from .project import Project
```

## ⚙️ 2. Registro no Admin
📄 Arquivo: blog/admin.py

```python
from django.contrib import admin
from .models import Project

admin.site.register(Project)
```
## 🔄 3. Migrações aplicadas
```bash
python manage.py makemigrations
python manage.py migrate
```
## 🧪 4. Teste manual via Shell
```bash
python manage.py shell
```
```python
from blog.models import Project

Project.objects.create(
    title="Projeto Shell",
    description="Criado manualmente",
    url="https://exemplo.com",
    is_published=True
)

print(Project.objects.all())
```
## 🧬 5. Testes com Django TestCase
📄 Arquivo: blog/tests/test_project_model.py

```python
from django.test import TestCase
from blog.models import Project

class TestProjectModel(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Projeto Teste",
            description="Modelo de teste",
            url="https://teste.com",
            is_published=True
        )

    def test_str_method(self):
        self.assertEqual(str(self.project), self.project.title)

    def test_field_values(self):
        self.assertEqual(self.project.description, "Modelo de teste")
        self.assertTrue(self.project.is_published)
```
## 🏭 6. Factory com Factory Boy
📦 Instalação:

```bash
pip install factory_boy
```
📄 Arquivo: blog/factories.py

```python
import factory
from blog.models import Project

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("paragraph")
    url = factory.Faker("url")
    is_published = factory.Faker("boolean")
```
## 🧪 7. Testes com Factory
📄 Arquivo: blog/tests/test_project_model.py

```python
from django.test import TestCase
from blog.factories import ProjectFactory

class TestProjectFactory(TestCase):
    def setUp(self):
        self.project = ProjectFactory()

    def test_str_method(self):
        self.assertEqual(str(self.project), self.project.title)

    def test_project_created(self):
        self.assertIsNotNone(self.project.pk)
```

## 🐍 8. Configuração do Pytest
📄 Arquivo: pytest.ini

```ini
[pytest]
DJANGO_SETTINGS_MODULE = ebac_m5_mysite.settings
python_files = tests.py test_*.py *_tests.py
```

📦 Instalação:

```bash
pip install pytest pytest-django
```

## 🎯 Execução:

```bash
pytest
```

##🛠️ 9. Correções realizadas durante o processo
✅ Removido conflito entre tests.py e pasta tests/

✅ Corrigida factory ProjectFactory que estava apontando para Post

✅ Limpado cache com .pyc e __pycache__

✅ Ajustada estrutura dos testes para pasta blog/tests/

✅ Testes reconhecidos com sucesso via pytest

✅ Resultado Final
Todos os testes foram executados com sucesso. O modelo Project está funcional no Django Admin, pode ser persistido no banco, testado manualmente e automatizadamente com Factory e Pytest. Estrutura pronta para expandir o projeto em futuras etapas do curso.
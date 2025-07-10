from django.test import TestCase
from blog.factories import ProjectFactory

class ProjectFactoryTest(TestCase):
    def setUp(self):
        self.project = ProjectFactory()

    def test_str_method(self):
        self.assertEqual(str(self.project), self.project.title)

    def test_project_created(self):
        self.assertTrue(self.project.pk is not None)
        self.assertIsInstance(self.project.url, str)
        self.assertIsInstance(self.project.is_published, bool)
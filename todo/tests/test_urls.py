from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import task_list, add_task, edit_task, delete_task, toggle_complete

class TestUrls(SimpleTestCase):

    def test_task_list_url_resolves_home(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, task_list)

    def test_task_list_url_resolves(self):
        url = reverse('task_list')
        self.assertEqual(resolve(url).func, task_list)

    def test_add_task_url_resolves(self):
        url = reverse('add_task')
        self.assertEqual(resolve(url).func, add_task)

    def test_edit_task_url_resolves(self):
        url = reverse('edit_task', args=[1])
        self.assertEqual(resolve(url).func, edit_task)

    def test_delete_task_url_resolves(self):
        url = reverse('delete_task', args=[1])
        self.assertEqual(resolve(url).func, delete_task)

    def test_toggle_complete_url_resolves(self):
        url = reverse('toggle_complete', args=[1])
        self.assertEqual(resolve(url).func, toggle_complete)
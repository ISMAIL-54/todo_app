from django.test import TestCase
from django.urls import reverse
from todo.models import Task

# Test views: 5 tests 
class TestViews(TestCase):
    def setUp(self):
        Task.objects.create(title="Task #1", description="Some description...", completed=True)
        Task.objects.create(title="Task #2", description="Some description...", deadline="2026-01-10")
    
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, "Task #1")
        self.assertContains(response, "Task #2")

    def test_add_task_view(self):
        response = self.client.post(reverse('add_task'), {
            'title': 'New Task',
            'description': 'New description',
            'deadline': '2026-02-15'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_edit_task_view(self):
        task = Task.objects.first()
        response = self.client.post(reverse('edit_task', args=[task.id]), {
            'title': 'Updated Task',
            'description': 'Updated description',
            'deadline': '2026-03-20'
        })
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')

    def test_delete_task_view(self):
        task = Task.objects.first()
        response = self.client.get(reverse('delete_task', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_toggle_complete_view(self):
        task = Task.objects.get(title="Task #2")
        initial_status = task.completed
        response = self.client.get(reverse('toggle_complete', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertNotEqual(task.completed, initial_status)
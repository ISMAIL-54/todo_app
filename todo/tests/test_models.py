from django.test import TestCase

# Test models: 1 test
class TestModels(TestCase):

    def test_task_creation(self):
        from todo.models import Task
        task = Task.objects.create(title="Test Task", description="This is a test task.", deadline="2026-12-31")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertFalse(task.completed)
        self.assertEqual(str(task.deadline), "2026-12-31")
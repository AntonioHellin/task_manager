import unittest
from unittest.mock import patch, mock_open
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    def test_init_empty(self, mock_file):
        tm = TaskManager()
        self.assertEqual(tm._tasks, [])
        self.assertEqual(tm._next_id, 1)

    @patch("task_manager.open", new_callable=mock_open, read_data='[{"id":1,"description":"Test","completed":false}]')
    def test_init_with_tasks(self, mock_file):
        tm = TaskManager()
        self.assertEqual(len(tm._tasks), 1)
        self.assertEqual(tm._tasks[0].description, "Test")
        self.assertEqual(tm._next_id, 2)

    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.print")
    def test_add_task(self, mock_print, mock_file):
        tm = TaskManager()
        tm._tasks = []
        tm._next_id = 1
        tm.add_task("New Task")
        self.assertEqual(len(tm._tasks), 1)
        self.assertEqual(tm._tasks[0].description, "New Task")
        mock_print.assert_any_call("Added task: New Task")
        mock_file().write.assert_called()

    @patch("task_manager.print")
    def test_list_tasks_empty(self, mock_print):
        tm = TaskManager()
        tm._tasks = []
        tm.list_tasks()
        mock_print.assert_called_with("No tasks available.")

    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.print")
    def test_list_tasks_nonempty(self, mock_print, mock_file):
        tm = TaskManager()
        class DummyTask:
            def __str__(self):
                return "Task1"
        tm._tasks = [DummyTask()]
        tm.list_tasks()
        # Check that one of the print calls stringifies to 'Task1'
        printed_args = [str(call_args[0][0]) for call_args in mock_print.call_args_list]
        self.assertIn("Task1", printed_args)

    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.print")
    def test_complete_task_success(self, mock_print, mock_file):
        class DummyTask:
            def __init__(self):
                self.id = 1
                self.description = "A"
                self.completed = False
        tm = TaskManager()
        tm._tasks = [DummyTask()]
        tm.complete_task(1)
        self.assertTrue(tm._tasks[0].completed)
        mock_print.assert_any_call("Completed task: A")
        mock_file().write.assert_called()

    @patch("task_manager.print")
    def test_complete_task_not_found(self, mock_print):
        tm = TaskManager()
        tm._tasks = []
        tm.complete_task(99)
        mock_print.assert_called_with("Task with ID 99 not found.")

    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.print")
    def test_delete_task_success(self, mock_print, mock_file):
        class DummyTask:
            def __init__(self):
                self.id = 1
                self.description = "A"
        task = DummyTask()
        tm = TaskManager()
        tm._tasks = [task]
        tm.delete_task(1)
        self.assertEqual(tm._tasks, [])
        mock_print.assert_any_call("Deleted task: A")
        mock_file().write.assert_called()

    @patch("task_manager.print")
    def test_delete_task_not_found(self, mock_print):
        tm = TaskManager()
        tm._tasks = []
        tm.delete_task(99)
        mock_print.assert_called_with("Task with ID 99 not found.")

    @patch("task_manager.open", new_callable=mock_open, read_data="[]")
    def test_save_tasks(self, mock_file):
        class DummyTask:
            def __init__(self):
                self.id = 1
                self.description = "A"
                self.completed = False
                self.__dict__ = {"id": 1, "description": "A", "completed": False}
        tm = TaskManager()
        tm._tasks = [DummyTask()]
        tm.save_tasks()
        handle = mock_file()
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn('"description": "A"', written)

    @patch("task_manager.open", new_callable=mock_open, read_data='[{"id":2,"description":"B","completed":true}]')
    def test_load_tasks(self, mock_file):
        tm = TaskManager()
        tm._tasks = []
        tm._next_id = 1
        tm.load_tasks()
        self.assertEqual(len(tm._tasks), 1)
        self.assertEqual(tm._tasks[0].description, "B")
        self.assertEqual(tm._next_id, 3)

if __name__ == "__main__":
    unittest.main()

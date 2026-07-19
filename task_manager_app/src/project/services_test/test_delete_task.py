import unittest
from unittest.mock import MagicMock
from src.project.services.delete_task_service import DeleteTaskService

class TestDeleteTaskService(unittest.TestCase):
        
    def test_delete_task_successfully(self):
        # Create a blank fake repository
        fake_repo = MagicMock()
        
        # Instantiates and swaps out repo with the fake one
        service = DeleteTaskService()
        service.task_repository = fake_repo
        
        result = service.delete_task(42)
        self.assertEqual(result, {"success": True})

if __name__ == '__main__':
    unittest.main()
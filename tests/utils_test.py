import unittest
from unittest.mock import patch
import os
from src.utils.Utils import create_folder_if_not_exists

class TestCreateFolderIfNotExists(unittest.TestCase):
    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_create_folder_when_not_exists(self, mock_makedirs, mock_exists):
        mock_exists.return_value = False
        folder_path = 'some/folder/path'

        result = create_folder_if_not_exists(folder_path)

        mock_exists.assert_called_once_with(folder_path)
        mock_makedirs.assert_called_once_with(folder_path)
        self.assertTrue(result)

    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_create_folder_when_exists(self, mock_makedirs, mock_exists):
        mock_exists.return_value = True
        folder_path = 'some/folder/path'

        result = create_folder_if_not_exists(folder_path)

        mock_exists.assert_called_once_with(folder_path)
        mock_makedirs.assert_not_called()
        self.assertFalse(result)

    @patch('os.path.exists', side_effect=Exception("Test exception"))
    @patch('os.makedirs')
    def test_create_folder_with_exception(self, mock_makedirs, mock_exists):
        folder_path = 'some/folder/path'

        with self.assertRaises(Exception) as context:
            create_folder_if_not_exists(folder_path)

        self.assertEqual(str(context.exception), "Test exception")
        mock_makedirs.assert_not_called()

    def test_create_folder_with_wrong_datatype(self):
        folder_path = 12345  # Passing an integer instead of a string

        with self.assertRaises(TypeError):
            create_folder_if_not_exists(folder_path)

if __name__ == '__main__':
    unittest.main()



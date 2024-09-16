import unittest
from flask import Flask
from src.app import app, check_winner, check_draw

class TestApp(unittest.TestCase):
    def setUp(self):
        # Test setup
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Any cleanup needed after tests
        pass

    def test_play_move(self):
        # Test making a move
        response = self.app.get('/play/0')
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertIn(b'Current Player: O', self.app.get('/').data)

    def test_winner_detection(self):
        # Test the winner detection logic
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_winner(board), 'X')

        board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertEqual(check_winner(board), 'X')

if __name__ == '__main__':
    unittest.main()
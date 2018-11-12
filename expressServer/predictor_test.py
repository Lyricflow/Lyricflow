import unittest
from predictor import find_song

class TestFindSong(unittest.TestCase):
    def test_song(self):
        self.assertEqual(find_song("jumpman jumpman jumpman"), "Jumpman by drake")
        self.assertEqual(find_song(""), "I can't understand your request")
        self.assertEqual(find_song("     "), "I can't understand your request")
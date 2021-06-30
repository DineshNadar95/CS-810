import unittest
from HW07_Dinesh_Nadar import anagram_1st, anagrams_dd, anagrams_cntr, covers_alphabet, book_index


class TestContainer(unittest.TestCase):
    def test_anagram_1st(self):
        """to verify that anagram_1st works properly"""
        self.assertTrue(anagram_1st("dormitory", "dirtyroom"))
        self.assertTrue(anagram_1st("", "dirtyroom"))
        self.assertTrue(anagram_1st("DORMITORY", "dirtyroom"))
        self.assertTrue(anagram_1st("122Dirtry", ""))
        self.assertTrue(anagram_1st("Iceman", "Cinema"))

    def test_anagram_dd(self):
        """to verify that anagram_dd works properly"""
        self.assertTrue(anagrams_dd("dormitory", "dirtyroom"))
        self.assertTrue(anagrams_dd("", "dirtyroom"))
        self.assertTrue(anagrams_dd("DORMITORY", "dirtyroom"))
        self.assertTrue(anagrams_dd("122Dirtry", ""))
        self.assertTrue(anagrams_dd("Iceman", "Cinema"))

    def test_anagram_cntr(self):
        """to verify that anagram_cntr works properly"""
        self.assertTrue(anagrams_cntr("dormitory", "dirtyroom"))
        self.assertTrue(anagrams_cntr("", "dirtyroom"))
        self.assertTrue(anagrams_cntr("DORMITORY", "dirtyroom"))
        self.assertTrue(anagrams_cntr("122Dirtry", ""))
        self.assertTrue(anagrams_cntr("Iceman", "Cinema"))

    def test_cover_alphabet(self):
        """to verify that test_cover_aplhabet works properly"""
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertTrue(covers_alphabet("xyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("12344"))
        self.assertTrue(covers_alphabet(""))

    def test_book_index(self):
        """to verify that test_book_index works properly"""
        self.assertTrue(book_index([('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), (
            'chuck', 1), ('wood', 1)]) == [['a', [1, 1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]])
        self.assertTrue(book_index("") == [['word1', [1, 3]], ['word2', [2]]])
        self.assertTrue(book_index([('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)]) == "")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

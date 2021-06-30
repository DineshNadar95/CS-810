import unittest
from HW05_Dinesh_Nadar import reverse, rev_enumerate, find_second, get_lines


class TestString(unittest.TestCase):
    def test_reverse(self):
        """to verify that reverse works properly"""
        self.assertTrue(reverse('abc') == 'cba')
        self.assertTrue(reverse('abd') == 'cba')
        self.assertTrue(reverse('abc') == 'abc')

    def test_rev_enumerate(self):
        """to verify that rev_enumerate works"""
        self.assertTrue(list(rev_enumerate("Python"))==[(5, 'n'), (4, 'o'), (3, 'h'), (2, 't'), (1, 'y'), (0, 'P')])
        self.assertTrue(list(rev_enumerate("hell"))==[(4, 'o'), (3, 'l'), (2, 'l'), (1, 'e'), (0, 'H')])
        self.assertTrue(list(rev_enumerate("My"))==[(1, 'm'), (0, 'y')])


    def test_find_second(self):
        """to verify that find_second works"""
        self.assertTrue(find_second('iss','Mississippi')==4)
        self.assertTrue(find_second('iss','Mississippi')==9)
        self.assertTrue(find_second('rr','Rondar')==4)

    def test_get_lines(self):
        """to verify that get_lines works"""
        file_name = 'test.txt'
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)
        except1=['<line0>', '<line1>', '<line2>','<lne33>']
        self.assertEqual(result,except1)

if __name__ == '__main__':
    """main function for test case"""
    unittest.main(exit=False, verbosity=2)

import unittest
from HW06_Dinesh_Nadar import list_copy,list_intersect,list_difference,remove_vowels,check_pwd,insertion_sort

class TestList(unittest.TestCase):
    def test_list_copy(self):
        """to verify that list_copy works properly"""
        self.assertTrue(list_copy([1,2,3]) == [1,2,3])
        self.assertTrue(list_copy([1,2,3]) == [1,2])
        self.assertTrue(list_copy([]) == [1,2])
        
    def test_list_intersect(self):
        """to verify that list_intersect works properly"""
        self.assertTrue(list_intersect([1,2,3],[2,3,4])==[2, 3])
        self.assertTrue(list_intersect([1,2,3],[6,4,3])==[2, 3,6])
        self.assertTrue(list_intersect([1,2,3],[])==[2, 3])
        
    def test_list_difference(self):     
        """to verify that list_difference works properly"""
        self.assertTrue(list_difference([1,2,3],[2,3,4])==[1])
        self.assertTrue(list_difference([1,2,3],[3,6,4])==[1,3,4])
        self.assertTrue(list_difference([],[1,2,3])==[1,3,4])
        
        
    def test_remove_vowels(self):
        """to verify that remove_vowels works properly"""
        self.assertTrue(remove_vowels('hello world')=="hll wrld")
        self.assertTrue(remove_vowels('hello world')=="hell0 world")
        self.assertTrue(remove_vowels('')=="world")
        
        
    def test_check_pwd(self):
         """to verify that check_pwd works properly"""
         self.assertTrue(check_pwd("DdaseQQ4q1")==True)
         self.assertTrue(check_pwd("D1")==True)
         self.assertTrue(check_pwd("dase1")==True)
         self.assertTrue(check_pwd("Ddase44QQ")==True)
         self.assertTrue(check_pwd("")==True)
    
    def test_insertion_sort(self):
         """to verify that insertion_sort works properly"""
         self.assertTrue(insertion_sort([7,4,3,2,6])==[2, 3, 4, 6, 7])
         self.assertTrue(insertion_sort([7,4,3,2,6])==[1,2,3,4,5])
         self.assertTrue(insertion_sort([])==[2, 3, 4, 6, 7])
    
    
    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
import unittest
from HW08_Dinesh_Nadar import date_arithmetic, file_reading_gen,FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    def test_date_arithmetic(self):
        """to verify that date_arithmetic works properly"""
        self.assertEqual(date_arithmetic(),('03/01/00', '03/02/17', 303))
        self.assertEqual(date_arithmetic(),('03/01/2000', '03/02/2017', 1303))
    

    def test_file_reading_gen(self):
        """to verify that file_reading_gen works properly"""
        directory = 'D:\Assgnments\SSW 10\HomeWork08\student_major.txt'
        self.assertEqual([x for x in file_reading_gen(directory, 3, "|", False)],[('123', 'Jin He', 'Computer Science'), 
('234', 'Nanda Koka', 'Software Engineering'), 
('345', 'Benji Cai', 'Software Engineering')])
        self.assertEqual([x for x in file_reading_gen("student_majors.txt", 3, "|", False)],[('123', 'Jin He', 'Computer Science'), 
('234', 'Nanda Koka', 'Software Engineering'), 
('345', 'Benji Cai', 'Software')])
        


    def test_file_analyzing_summary(self):
        """to verify that file_analyzer works properly"""
        directory = 'D:\Assgnments\SSW 10\HomeWork08' #Here you can change the directory
        analyzer = FileAnalyzer(directory) 
        # print(analyzer.files_summary)
        self.assertEqual(analyzer.files_summary,{'file1.py': {'Characters': 270, 'Lines': 25, 'Classes': 2, 'Functions': 4}, 'HW08_Dinesh_Nadar.py': {'Characters': 4372, 'Lines': 113, 'Classes': 1, 'Functions': 5}, 'HW08_Test_Dinesh_Nadar.py': {'Characters': 1627, 'Lines': 33, 'Classes': 1, 'Functions': 3}})
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

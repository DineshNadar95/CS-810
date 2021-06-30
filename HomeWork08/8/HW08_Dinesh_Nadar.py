from datetime import datetime, timedelta
import os
from prettytable import PrettyTable


def date_arithmetic():
    """this function gives proper dates accordingly"""
    date_1 = "February 27, 2000"
    date_2 = "February 27, 2017"
    date_3 = "January 1, 2017"
    date_4 = "October 31, 2017"
    dt1 = datetime.strptime(date_1, "%B %d, %Y")
    dt2 = datetime.strptime(date_2, "%B %d, %Y")
    dt3 = datetime.strptime(date_3, "%B %d, %Y")
    dt4 = datetime.strptime(date_4, "%B %d, %Y")

    three_days_after_02272000 = dt1 + timedelta(days=3)
    three_days_after_02272017 = dt2 + timedelta(days=3)
    delta = dt4 - dt3
    days_passed_01012017_10312017 = delta.days
    # return(
    #     f"3 days after {dt1:%m/%d/%y} is {three_days_after_02272000:%m/%d/%y}")
    # return(
    #     f"3 days after {dt2:%m/%d/%y} is {three_days_after_02272017:%m/%d/%y}")
    # return(
    #     f"Number of days between {dt3:%m/%d/%y} and {dt4:%m/%d/%y} is {days_passed_01012017_10312017}")
    return((three_days_after_02272000.strftime('%m/%d/%y')),three_days_after_02272017.strftime('%m/%d/%y'),days_passed_01012017_10312017)





def file_reading_gen(path, fields, sep, header):
    """ reading the file and creating the output as requested."""
    line_count = 0
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise("Error File not found", path)
    else:
        with fp:
            for line in fp:
                line_count = line_count+1
                f = line.strip('\n').split(sep)
                if len(f) != fields:
                    raise ValueError(
                        f"ValueError:{path} has {len(f)} fields on the line {line_count} but expected {fields}")
                else:
                    if header == False:
                        header = True
                    else:
                        yield(tuple(f))


class FileAnalyzer:
    """Class which consist of 3 functions solely for file analyzing purpose"""
    def __init__(self, directory):
        """ Initializes the variable or fucntion"""
        self.directory = directory  
        self.files_summary={}
        self.analyze_files()  # summerize the python files data

    def analyze_files(self):
        """ Your To Analyze the file and create a counts of character and so on."""
        try:
            d_open = os.listdir(self.directory)
            os.chdir(self.directory)
        except NotADirectoryError:
            raise("Directory is not Found.")
        else:
            for file_name in d_open:
                if file_name.endswith(".py"):
                    try:
                        fp = open(file_name, 'r')
                    except FileNotFoundError:
                        raise("Error File not Found.")
                    else:
                        with fp:
                            line_count = 0
                            ch_count = 0
                            func_count = 0
                            class_count = 0
                            for line in fp:
                                
                                line_count = line_count + 1
                                ch_count = ch_count + len(line)
                                s_line = line.strip()
                                if s_line.startswith("def") and s_line.endswith("):"):
                                    func_count = func_count + 1
                                if s_line.startswith("class ") and s_line.endswith(":"):
                                    class_count = class_count + 1
                            self.files_summary[file_name] = {"Characters":ch_count,"Lines": line_count, "Classes":class_count,"Functions": func_count}
            self.prettytable()
            print(self.files_summary)

    def prettytable(self):
        """ To Create a PrettyTable."""

        pt = PrettyTable(
            field_names = ['FileName', 'Characters', 'Lines', 'Classes', 'Functions'])
        # print(self.files_summary)
        for key,value in self.files_summary.items():
            pt.add_row([key,value['Characters'],value['Lines'], value['Classes'],value['Functions']])
        
        return(pt)

def main():
    directory = 'D:\Assgnments\SSW 10\HomeWork08'
    x=FileAnalyzer(directory)
    print(x.prettytable())
    
          
if __name__ == '__main__':
    main()
directory = 'D:\Assgnments\SSW 10\HomeWork08' #Here you can change the directory
FileAnalyzer(directory)



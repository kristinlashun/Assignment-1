# Author: Kristin Towns 
# GitHub username: kristinlashun
# Date: 1/10/2024
# Description: 
import statistics

class Student: 
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self): 
        return self._grade 
    

def basic_stats(student_list): 
    grades = [student.get_grade() for student in student_list]
    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)

    return (mean,median,mode)

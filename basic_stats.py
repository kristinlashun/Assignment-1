# Author: Kristin Towns 
# GitHub username: kristinlashun
# Date: 1/10/2024
"""""
Description: This module contains the Student class for storing student names and grades, and a function basic_stats
that computes the mean, median, and mode of grades from a list of Student objects, using Python's statistics module.
"""
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

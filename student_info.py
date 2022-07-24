import numpy as np


class student:
    def __init__(self, name, stipend):
        self.name = name
        self.stipend = stipend
        self.score = {}
    #

    def print_ave_score(self):
        ave = sum(self.score.values()) / len(self.score.values())
        print(f'average score: {ave}')

    def input_score(self, class_type, score):
        self.score[class_type] = score


s1 = student(name="AAA", stipend=5000)
s2 = student(name="BBB", stipend=8000)

print(s1.name)
print(s1.score)
s1.input_score('english', 80)
s1.input_score('math', 50)
print(s1.score)

s1.print_ave_score()

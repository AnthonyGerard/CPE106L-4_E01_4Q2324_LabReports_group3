"""
File: student.py
Resources to manage a student's name and test scores.
"""
class Student(object):
    def __init__(self, name, number):
    	self.name = name
    	self.scores = []
    	for count in range(number):
            self.scores.append(0)
	
	def getName(self):
    	return self.name
	
	def setScore(self, i, score):
    	self.scores[i - 1] = score
	
	def getScore(self, i):
    	return self.scores[i - 1]
	
	def getAverage(self):
    	return sum(self.scores) / len(self.scores)
	
	def getHighScore(self):
    	return max(self.scores)
	
	def __str__(self):
       	return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"

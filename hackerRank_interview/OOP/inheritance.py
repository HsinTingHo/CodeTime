class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    def calculate(self):
        average = sum(self.scores)/len(self.scores)
        grade = ''
        if average <= 100 and average >= 90:
            grade = 'O'
        elif average < 90 and average >= 80:
            grade = 'E'
        elif average < 80 and average >= 70:
            grade = 'A'
        elif average < 70 and average >= 55:
            grade = 'P'
        elif average < 55 and average >= 40:
            grade = 'D'
        else:
            grade = 'T'
        return grade


firstName = 'Heraldo'
lastName = 'Memelli'
idNum = '8135627'

scores = [100, 80]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
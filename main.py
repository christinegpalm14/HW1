# Author: Christine Palmer cgp5153@psu.edu
# No Collaborators



gradepoint1 = input('Enter your course 1 letter grade:')
credit1 = float(input('Enter your course 1 credit:'))

if gradepoint1 == 'A': 
  grade1 = 4.0 
elif gradepoint1 == 'A-': 
  grade1 = 3.67
elif gradepoint1 == 'B+': 
  grade1 = 3.33
elif gradepoint1 == 'B': 
  grade2 = 3.0
elif gradepoint1 == 'B-': 
  grade1 = 2.67
elif gradepoint1 == 'C+': 
  grade1 = 2.33
elif gradepoint1 == 'C': 
  grade1 = 2.0 
elif gradepoint1 == 'D': 
  grade1 = 1.0
else: 
  grade1 = 0.0 

print(f'Grade point for course 1 is: {grade1}')


gradepoint2 = input('Enter your course 2 letter grade:')
credit2 = float(input('Enter your course 2 credit:'))

if gradepoint2 == 'A': 
  grade2 = 4.0 
elif gradepoint2 == 'A-': 
  grade2 = 3.67
elif gradepoint2 == 'B+': 
  grade2 = 3.33
elif gradepoint2 == 'B': 
  grade2 = 3.0
elif gradepoint2 == 'B-': 
  grade2 = 2.67
elif gradepoint2 == 'C+': 
  grade2 = 2.33
elif gradepoint2 == 'C': 
  grade2 = 2.0 
elif gradepoint2 == 'D': 
  grade2 = 1.0
else: 
  grade2 = 0.0 

print(f'Grade point for course 2 is: {grade2}')

gradepoint3 = input('Enter your course 3 letter grade:')
credit3 = float(input('Enter your course 3 credit:'))


if gradepoint3 == 'A': 
  grade3 = 4.0 
elif gradepoint3 == 'A-': 
  grade3 = 3.67
elif gradepoint3 == 'B+': 
  grade3 = 3.33
elif gradepoint3 == 'B': 
  grade3 = 3.0
elif gradepoint3 == 'B-': 
  grade3 = 2.67
elif gradepoint3 == 'C+': 
  grade3 = 2.33
elif gradepoint3 == 'C': 
  grade3 = 2.0 
elif gradepoint3 == 'D': 
  grade3 = 1.0
else: 
  grade3 = 0.0 

print(f'Grade point for course 3 is: {grade3}')

GPA = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)  

print(f'Your GPA is: {GPA}')



##print('Hi, %s.' % name)
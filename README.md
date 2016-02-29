# feedback-scores-analyzer
Name of Project: Feedback Analyser

Description: This project looks at a situation where a university's administration desires feedback from students about courses they have been enrolled to. Students have been invited to a discussion room where they write their feedback on a scale of 0 - 5 on a sheet of paper. The administration asks them to write their names so as to authenticate the students' details. The responses are collected on an excel sheet called "feedback scores". Another sheet "enrollments" lists the names of all students who had enrolled for the courses (the courses for which feeback is sought).

This program is designed to find the average of the feedback scores for the courses for which feedback was sought. However, before the averaging operation, the data must be subject to certain cleaning operations. The project looks at two hypothetical situaions where data cleaning is desired. In the first case, students who are not part of the university have filled up the feedback forms and in the second case students of university have given feedback even though they are not enrolled on a certain course.

Phase 1:
In Phase 1, data from the excel sheets has been compiled in two dictionaries: dict d1 and dict 2.

The two dictionaries are such:
d1: data from "enrollments"
d1 has a list of students and courses they are enrolled to:
d1's keys are strings (names) and values lists of integers.
[0,1,0] represents enrolled in course no 2 (and not in 0 and 1)

d2: data from "feedback scores"
d2 has a list of scores students assigned to courses:
grades = [2,0,5] represents
course no 1: scores 2
course no 2: scores 0
course no 3: scores 5

Phase 2 and further (under work):
In subsequent phases, data will be read directly from user-fed excel sheets (through a web page).

.....

How the program was broken up:

Task 1:studentchecker
At the studentchecker stage, we use a "for" loop to process information from dictionaries d1 and d2 and 
outputs a dictionary outRealStuds: a cleaned version of dictionary d2 where only those names will show who are actually enrolled students (names from dict 1)

Task 2:presencechecker 
At the presencechecker stage, we use a "for" loop to process information from dictionaries d1, d2 and outRealStuds and
generate a dictionary outRealGrades: a cleaned version of dictionary d2 where only the grades of those students will show who actually took the course

Task 3:averagescore calculator
The averaging operation is performed through an averaging function that takes three parameters:
(i)keyi, a variable that varies across a range from 0 to the number of courses
(ii)studCount, the count of students
(iii)outRealGrades, the dictionary of bonafide students with legitimate feedback scores
For every run of the averaging function, the function calculates the average of the feedback scores for one course.
...

Future direction for further development of the code:

Task 1:studentchecker
Write a function called data cleaner studentchecker that takes in two dictionaries (d1 and d2). 
The function will return a tuple of two dictionaries:
a cleaned version of dictionary d2 where only those names will show who are actually enrolled students (names from dict 1)
and
a list containing all respondents who are not students

Task 2: presencechecker 
Write a function called data cleaner presencechecker that takes in two dictionaries (d1 and d2). 
The function will return a tuple of two dictionaries:
a cleaned version of dictionary d2 where only the grades of those students will show who actually took the course
and
a list containing all students who had graded courses they had not been enrolled.
'''

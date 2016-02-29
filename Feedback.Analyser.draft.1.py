
'''
Name of Project: Feedback Analyser

Description: Imagine a situation where a university's administration desires feedback from students about courses they have been
enrolled to. Students have been invited to a discussion room where they write their feedback on a scale of 0 -5 on a sheet of paper.
The administration asks them to write their names so as to authenticate the students' details. The responses are collected on an
excel sheet called "feedback scores". Another sheet "enrollments" lists the names of all students who had enrolled for the courses
(the courses for which feeback is sought).

This program is designed to find the average of the feedback scores for the courses for which feedback was sought. However, before the averaging
operation, the data must be subject to certain cleaning operations. The project looks at two hypothetical situaions where data cleaning is desired.
In the first case, students who are not part of the university have filled up the feedback forms and in the second case students of university
have given feedback even though they are not enrolled on a certain course.

Phase 1:
In Phase 1, data from the excel sheets has been compiled in two dictionary: dict d1 and dict 2.

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


Future Direction for further refining of code:

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


#program start
def dict_coursegrader(d1,d2):
    outRealStuds = {}  #a dictionary which will have feedback scores of only bonafide students 
    outRealGrades = {} #a dictionary which will have feedback scores of only students enrolled for courses 
   
        #Stage 1:studentchecker
        #d2 has to be cleaned of students who are not university students
	#Action: transfer those elements from d2 that have keys common with d1 --> to the *common dict* outRealStuds
    for keyi in d1.keys():    
            for keyj in d2.keys():
                   if keyi == keyj: #if the keys are equal, add that key to dict outRealStuds
                        outRealStuds [keyj] =  d2[keyj]
                        break

    print ("list of bonafide students and the grades they assigned:")
    print (outRealStuds) # RESULT {'kari': [2, 3], 'gud': [2, 4]}


        #Stage 2:presencechecker
	#d2 has to be cleaned of those feedback scores where the students had not enrolled for the course
        #In stage 1, d2 has already been cleaned to outRealStuds. We can use the outRealStuds dict for further processing.
        #Action: If a student in outRealStuds has not enrolled for a particular course (information given in d1),
        #the grade given by that student for that particular course should be annuled
        #(for example, the grade could be changed to 10, which means not applicable)
        # --> transfer the changed data to *common dict checked for enrollments* outRealGrades

    print (outRealStuds['gud'])  #for testing! RESULT: [2, 4] CORRECT
    print (outRealStuds['gud'][1])  #for testing! RESULT: 4 CORRECT

    import copy
    #outRealGrades = dict(outRealStuds) #new dict that copies all elements of the old dict and is not bound to it.
    outRealGrades = copy.deepcopy(outRealStuds)
    
    for key in outRealGrades.keys():
        courseCount = len (outRealGrades[key])
        
    print courseCount  #for testing!
    
    for keyi in outRealGrades.keys():    
         for i in range (courseCount): 
                   if d1[keyi] [i] == 0: #the student is not enrolled to the course
                      print ("SOMEONE put a grade for a course he/she hasn't enrolled") # for testing!
                      outRealGrades [keyi] [i] = 10 #
                   

    print ("list of bonafide students and the grades they assigned:")
    print (outRealStuds) # for testing!
    
    print ("list of grades (filtered data) assigned by bonafide students:")    
    print (outRealGrades) #for testing!

        #Stage 3:averagescore calculator
        #An averaging operation for calculating average score for each course should be run on the dict "outRealGrades"  
        #The data from averaging of courses in outRealGrades is used to -->
        #generate averageGrades (dict with courses as keys and courses' avg scores as values)
        #In cases, where the grades score is 10 (10 stands for course score is not legitimate), that particular score is skipped from calulations
        
        
    averageGrades = {}

    studCount = len (outRealGrades)

    print ("no of students:")
    print (studCount)

    for key in outRealGrades.keys():
        courseCount = len (outRealGrades[key])

    print ("no of courses:")
    print (courseCount)

    for keyi in range (courseCount): #for calculating average for each course, we enter averagefn
        averageGrades [keyi] = averagefn (keyi, studCount, outRealGrades)
    print 
    print ("The dictionary of courses with the average feedback score for the courses is:")
    print (averageGrades)
    
    
def f(a, b): 
    return a + b

def averagefn (keyi, studCount, outRealGrades):
    sumGrades = 0
    invalidgradeCount = 0 
    for key in outRealGrades.keys():
        #print (i,keyi)
        if outRealGrades[key][keyi] == 10:
            invalidgradeCount = invalidgradeCount + 1  
        else:
            sumGrades = sumGrades + outRealGrades[key][keyi] #add the grades of different students for each of the subjects    

    print ("sum of scores:") #for testing!
    print (sumGrades)
    print ("avg of scores:") #for testing!
    averageGrades = sumGrades / ((studCount - invalidgradeCount )* 1.0)
    print (averageGrades)
    return averageGrades
        
	
d1 = {'adi':[1,0], 'kari':[1,1], 'gud':[1,0], 'chu':[1,1], 'ubu':[1,1] }#, students enrolled in METROPOLIA

d2 = {'gud':[2,4], 'kari':[2,3], 'asa': [5,0], 'chu' : [4,5], 'ubu':[2,3] }# feedback scores given by students 
    

dict_coursegrader (d1,d2)





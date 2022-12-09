'''7) take the input and evaluate  expressions 
 take student name 
 take student english marks ,maths,science,social,kannada,hindi while taking the input marks it shud be in the range frim1 to 100
 calculate % and print 
 %<35 print fail and print grade "F"
 %>35 and %<55 print just pass and print grade "D"
 %>55 and %<60 print  pass and print grade "C"
 %>60 and %<75 print average and print grade "B"
 %>75 and %<90 print good and print grade "A"
 %>90 and %<100 print excellent  and print grade "A+" '''

name=input("enter student name :\t")
english_marks=int(input("enter student english marks :\t"))
maths_marks=int(input("enter student maths marks :\t"))
science_marks=int(input("enter student science marks :\t"))
social_marks=int(input("enter student social marks :\t"))
kannada_marks=int(input("enter student kannada marks :\t"))
hindi_marks=int(input("enter student hindi marks :\t"))
#if(english_marks>0 and maths_marks>0 and science_marks>0 and social_marks>0 and kannada_marks>0 and hindi_marks>0):
if(english_marks<=100 and maths_marks<=100 and science_marks<=100 and social_marks<=100 and kannada_marks<=100  and hindi_marks<=100 
 and hindi_marks<=100 and english_marks>0 and maths_marks>0 and science_marks>0 and social_marks>0 and kannada_marks>0 and hindi_marks>0):
    total_percentage=(english_marks+maths_marks+science_marks+social_marks+kannada_marks+hindi_marks)/6
    if (total_percentage<35):
        print(name,"failed in exams and his grade is : F ")
    elif (total_percentage>35 and total_percentage<55):          
        print(name,"is just passed in exams and his grade is : D ")
    elif (total_percentage>55 and total_percentage<60):
        print(name,"is passed in exams and his grade is : C ")
    elif (total_percentage>60 and total_percentage<75):
        print(name,"geting average marks in exams and his grade is : B ")
    elif (total_percentage>75 and total_percentage<90):
        print(name,"geting good marks in exams and his grade is : A ")
    elif (total_percentage>90 and total_percentage<=100):
            print(name,"geting excellent  marks in exams and his grade is : A+ ")
else:
   print("enter student marks correctly that should be in range of 1 to 100 only" )
 
 
 
 

 
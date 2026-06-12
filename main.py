name=input('Enter your name:')
rno=int(input('Enter your rollno:'))
print('Please enter your mark out of 100:')
sub1=float(input('Enter subject 1 mark:'))
sub2=float(input('Enter subject 2 mark:'))
sub3=float(input('Enter subject 3 mark:'))
sub4=float(input('Enter subject 4 mark:'))
sub5=float(input('Enter subject 5 mark:'))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
print('\n -----RESULT-----')
print('Student Name:',name)
print('Student Rollno:',rno)
print('Total marks:',total,'/500')
print('Average:',avg)

if avg>=90:
    grade='A'
elif avg>=80:
    grade='B'
elif avg>=70:
    grade='C'
elif avg>=60:
    grade='D'
elif avg>=50:
    grade='E'
else:
    grade='F'

print('Highest Mark:',max(sub1,sub2,sub3,sub4,sub5))
print('Lowest Mark:',min(sub1,sub2,sub3,sub4,sub5))
print('Grade:',grade)

if avg>=40:
    print('Status:PASS')
else:
    print('Status:FAIL')

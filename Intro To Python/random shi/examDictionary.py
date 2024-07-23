A = {'Charlie':{'exam1':94,'exam2':96,'exam3':0,'exam4':91},'Sam':{'exam1':100,'exam2':98,'exam3':87,'exam4':97},'Blair':{'exam1':89,'exam2':0,'exam3':89,'exam4':77},'Karen':{'exam1':82,'exam2':92,'exam3':81,'exam4':'N'},'Sarah':{'exam1':70,'exam2':30,'exam3':80,'exam4':92}}
Info =input(('would you like to check (a score), (find how many) students, average (of a student), or add (a student)'))
student = ''
test = ''
new = ""
average= int
if(Info=='check'):
    student = str(input(f'want to check Charlie, Sam, Blair, Karen or Sarah'))
    test = str(input('want to check  exam1, exam2, exam3, exam4, or exam5'))
    print(A[student][test])
if(Info=='average'):
    student = str(input(f'want to check charlie, sam, blair, karen or sarah'))
    average= (A[student]['exam1'] + A[student]['exam2'] +A[student]['exam3'] +A[student]['exam4'] )/ len(A[student])
    print(f'{average} is average of {student}')
    if(average>=50):
        print('pass')
    else:
        print('fail')
if(Info=='students'):
    print(len(A))

        
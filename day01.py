#교재 딕셔너리 예제

subjects = {'의사소통 영어':'A+',
           '오래된 미래':'B+',
           '양자역학':'A0'
           }
student = '김성민'
subject = '오래된 미래'
print(f'ultra modern style: {student}이 수강중인 "{subject}" 수업의 학점은 {subjects[subject]}입니다.')
# f스트링 = 최신 문법, 문자열과 변수 한번에 출력하고자 할 때 사용한다.
#ultra modern style

print("modern style: {0}학생의 {1}과목성적은 {2}입니다.".format(student, subject, subjects[subject]))
#modern style(format함수)

print('old style: %s 학생의 %s과목 성적은 %s입니다.' % (student, subject, subjects[subject]))
#old style

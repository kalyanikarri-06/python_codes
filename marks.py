m = int(input("maths: "))
s = int(input("science: "))
t = int(input("telugu: "))
total = m+s+t
avg = total/3
per = (total/300)*100
if(per>90):
  grade="A"
elif(per>80 and per<=90):
    grade ='B'
elif(per>70 and per<=80):
    grade='C'
else:
    grade='D'
print(f"grade of the student : {grade}")

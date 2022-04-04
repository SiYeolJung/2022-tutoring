#정수 N을 입력으로 받아서
# 00시 00분 00초 ~ N시 00분 00초까지 3이 포함된 개수 리턴
# 5 11475 

N = int(input())
count =0
for i in range (N+1):
    for j in range (60):
        for k in range (60):
            if "3" in str(k) or "3" in str(j) or "3" in str(i):
                count+=1
print(count)    


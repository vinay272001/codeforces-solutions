n = int(input())
cnt=0
for i in range(n):
    a = input()
    if a[0]=='+' or a[-1]=='+':
        cnt+=1
    else:
        cnt-=1
print(cnt)

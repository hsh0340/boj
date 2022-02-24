import sys

listLen = int(input()) # 수열의 길이 주어짐
# 공백을 사이에 두고 수열을 입력받음 -> 리스트로 
numList = list(map(int,sys.stdin.readline().split())) 
numList = sorted(numList) # 오름차순으로 정렬
for i in range(len(numList)) : 
    numList[i] = str(numList[i]) # 공백을 사이에 두기 위해서 원소를 str로 바꿔줌
print(' '.join(numList)) # 공백을 사이에 둔다
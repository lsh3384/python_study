# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array1 = [i for i in range(20) if i % 2 == 1]

print(array1)

# 0부터 19까지의 수 중에서 3의 배수만 포함하는 리스트
array2 = [i for i in range(20) if i % 3 == 0]
print(array2)

# 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용해야 한다.

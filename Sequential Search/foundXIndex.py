# 문제 : 어떤 수 x가 n개의 수로 구성된 리스트(배열) S에 존재하는가?
# 답 : x가 존재하면 x의 인덱스를 출력, 존재하지 않으면 0을 출력
# - 즉, x가 해답 or 0이 해답
# 파라미터 : 정수 n(> 0), 리스트 S(인덱스 범위는 1부터 n까지), 원소 x
# - (> 0)은 0보다 큰 수를 의미합니다.
# 위 파라미터를 이용해서 입력사례를 적어봅시다.
# 입력 사례 : S = [0, 10, 7, 11, 5, 13, 7], n = 6, x = 5
# - 이 입력 사례같은 경우 S안에 목표인 x값이 들어있으므로 x의 인덱스값인 4가 해답.
# - 만약 위 사례에서 x를 13을 줄 경우 해답은 5, 22를 줄 경우 해답은 0이 나옵니다.

# 위 문제와 해답을 기준으로 알고리즘을 짜봅시다.
# - S의 첫째 원소에서 시작하여 x를 찾을 때까지(x가 없는 경우 끝까지) 각 원소를 차례로 x와 비교한다.
# - 만약, x를 찾으면 x의 인덱스를 리턴하고, 찾지 못한다면 0을 리턴한다.


# 생각 코딩 ( 강의에 코드를 보지 않고 )

print("생각 코딩 부분")


def ThinkingSequentialSearch(n, S, x):
    for i in range(0, n):
        if (S[i] == x):
            return S.index(x)
    return 0


S = [0, 10, 7, 11, 5, 13, 7]
n = 6
x = 5

print(ThinkingSequentialSearch(n, S, x), "\n")

# 강의 코드
print("강의 코드부분")


def seqsearch(n, S, x):
    location = 1  # 1번째 원소
    # location이 n보다 작거나 같고, S[location]이 x가 아닐때까지
    while(location <= n and S[location] != x):
        location += 1
    if (location > n):  # 만약 해당하는 원소 x가 없을 경우
        location = 0  # 0을 리턴한다.
    return location  # location을 리턴한다.


print(seqsearch(len(S) - 1, S, x))

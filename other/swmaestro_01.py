# SW마에스트로 14기 1차 문제

def solution(n, snow):
	answer = []
	t = 0

	for i in range(0, n, 1):
		# 다음으로 넘어왔을 때 전에 내려준 값(t)이 있다면 더해줌
		snow[i] += t
		# t를 다시 초기화.
		t = 0

		if snow[i] > (2*(n-(n-i))+1):
			print(snow[i])
			# 내려줄 값
			t = snow[i] - (2*(n-(n-i))+1)
				# ㅇㅊㅍ 넘쳤으니 최대값을 담아줌
			answer += [(2*(n-(n-i))+1)]

		else:
			answer += [snow[i]]

	return answer

snow = [2, 3, 5, 1, 13, 12]
print(solution(6, snow))

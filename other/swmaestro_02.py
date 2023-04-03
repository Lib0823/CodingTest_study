# # - **여러개의 화살표를 나타내는 문자열을 던져줌**
# #     **Ex) “`<--<---><-<-—`”**
# #     **화살표는 ( <--, -->, <--> ) 이러한 형태를 하나로 간주한다.**
# #     **“<”는 -1**
# #     **“>”는 1**
# #     **“<>”는 0 으로 표현하며, 화살표 방향값과 대시”-”의 길이를 각 배열에 담아 출력하라.**
# #     **Ex> `answer[[-1, 2], [0, 3], [-1, 1], [-1, 4]]`**

# def solution(image):
# 	answer = []

# 	a = 0
# 	cnt = 0

# 	for i in image:
# 		if i=='<':
# 			if a == -1:
# 				answer += [[-1, cnt]]
# 				cnt = 0
# 			a = -1

# 		elif i=='>':
# 			# 괄호가 열려있다면
# 			if a == -1:
# 				answer += [[0, cnt]]
# 				# 초기화
# 				a = 0
# 				cnt = 0

# 			# 괄호가 없었다면
# 			elif a == 0:
# 			    answer += [[1, cnt]]
# 			    # 초기화
#                 a = 0
# 		        cnt = 0
# 	    else:
# 			cnt += 1

# 	# 마지막
# 	if cnt != 0:
# 		answer += [[-1, cnt]]

# 	return answer
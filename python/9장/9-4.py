import time

# 그리니치 천문대 기준 1970년 1월 1일 0시 0분 0초 부터 경과 된 시간
seconds = time.time()
print(seconds)

tm = time.gmtime()
print(tm)

tm2 = time.localtime(1739245463.1952088)
print("년",tm2.tm_year)
print("월",tm2.tm_mon)
print("일",tm2.tm_mday)
print("시",tm2.tm_hour)
print("분",tm2.tm_min)
print("초",tm2.tm_sec)

# 產生一個隨機整數 1~100 (不要印)
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"終於猜對了！"
# 猜錯的話，要告訴他"比答案大/三小"


import random

r = random.randint(1, 100)
while True:# 先寫一個無限循迴，當使用者猜對後，再用break離開
    num = input('請猜數字： ')
    num = int(num)
    if num == r:
    	print('你猜中了！')
    	break
    elif num > r:
    	print('比答案大')
    elif num < r:
    	print('比答案小')
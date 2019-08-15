import random
# import numpy as np
# res = np.random.choice(['石头','✂️','🙅🙅‍♀️'])
# print(res)
import os
C_res = random.randint(0,2)
U_res = int(input('0:石头,1:剪刀,2:布'))
if C_res == U_res:
    print('平局')
else:
    if C_res == 0 and U_res == 1:
        print('电脑赢了 😢')
        os.system('say you loser.')
    elif C_res == 1 and U_res == 2:
        print('电脑赢了 😢')
        os.system('say you loser.')
    elif C_res == 2 and U_res == 0:
        print('电脑赢了 😢')
        os.system('say you loser.')
    else:
        print('你赢了 😄')
        os.system('say you winer.')









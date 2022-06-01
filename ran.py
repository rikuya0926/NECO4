import random

h=[0,2,5]

x=int(input("出す手を決めてください（グー=0、パー=5、チョキ=2）:"))
if x not in(h):
    print("正しい数値を入力してください")
else:

    y=random.choice(h)
    if x==0:
        hand="グー"
    elif x==2:
        hand="チョキ"
    else:
        hand="パー"
    if y==0:
        enemyhand="グー"
    elif y==2:
        enemyhand="チョキ"
    else:
        enemyhand="パー"
    print("あなた:"+hand+"、相手:"+enemyhand)

    class win():
        def __init__(self):
            print("あなたの勝ちです")

    class lose():
        def __init__(self):

            print("あなたの負けです")

    class draw():
        def __init__(self):

            print("あいこです")



    class judge():
        def __init__(self):
            if x==0 and y==2:
                win()
            elif x==0 and y==5:
                lose()
            elif x==2 and y==5:
                win()
            elif x==2 and y==0:
                lose()
            elif x==5 and y==0:
                win()
            elif x==5 and y==2:
                lose()
            else:
                draw()
    judge()

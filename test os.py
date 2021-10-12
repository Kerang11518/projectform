import random  # เอาตัว import ออกได้แล้วลบ random.sample(range(1,30),5)
LS = random.sample(range(1, 30), 5)  # [10,20,5,13,3,12,5,32]
Max = LS[0]
Min = LS[0]
n = len(LS)
count = 1
print(f'random : {LS}')
print(f'Numbers set : ค่า Max : {Max}  ค่า Min : {Min}')
for i in range(1, n):
    if LS[i] > Max:
        Max = LS[i]
        print(f'Round {count} ค่า Max : {Max} ค่า Min : {Min}')
    elif LS[i] < Min:
        Min = LS[i]
        print(f'Round {count} ค่า Max : {Max} ค่า Min : {Min}')
    else:
        print(f'Round {count} ค่า Max : {Max} ค่า Min : {Min}')
    count +=1
#print(LS)
print('\n-----------------------')
print(f'The Minimum is : {Min}')
print(f'The Maximum is : {Max}')
print('-----------------------')
#Instructions:https://adventofcode.com/2020/day/11
import os
import numpy as np

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]

    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            line=line.rstrip()
            l=[]
            for ch in line:
                l.append( ch)
            data.append(l)
        matrix=np.array(data)
    return matrix

data=get_data("test.txt")
#print(data)
#data=np.array([['#','#','#','#'],['D','E','#','#'],['G','H','I','Q'],['K','L','M','L']])
#print(data)
#row_num=3
#col_num=0
#print(data[row_num][col_num])
#print(len(data[:]))
#print(len(data[0][:]))
#data_next=np.copy(data)
#data_next[1][1]="Z"
#print(data[1][1])
#print(data_next[1][1])



def adjacent_seat(row_num,col_num,row_num_target,col_num_target):
    if row_num==row_num_target and col_num==col_num_target:
        return False
    elif abs(col_num -col_num_target)<2 and abs(row_num-row_num_target)<2:
        return True

def count_occupied_adjacent_seats(row_num_target,col_num_target):
    count=0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if adjacent_seat(i,j,row_num_target,col_num_target)== True and data[i][j]=="#":
                count+=1
    return count


#print(count_occupied_adjacent_seats(row_num,col_num))
#print("before")
#print(data) 
def one_round(data):
    data_next=np.copy(data)
    count_changes=0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="L" and count_occupied_adjacent_seats(i,j)==0:
                data_next[i][j]="#"
                count_changes+=1

            if data[i][j]=="#" and count_occupied_adjacent_seats(i,j)>=4:
                data_next[i][j]="L"
                count_changes+=1
    return data_next,count_changes
#print("after")
#print(one_round(data)[0])
#print("num of changes",one_round(data)[1])


def count_occupied(data):
    
    count=0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="#" :
                count+=1
    return count



changes=1
round_n=0
while changes!=0:
    round_n+=1
    print("round",round_n)
    data=one_round(data)[0]
    changes=one_round(data)[1]
    print("changes",changes)

print(count_occupied(data))



        




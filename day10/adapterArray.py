#Instructions:https://adventofcode.com/2020/day/10
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]

    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( int(line.rstrip()) )
    return data

def addCount(item,count_1,count_2,count_3):
    if item==1:
        count_1+=1
    elif item==2:
        count_2+=1
    elif item==3:
        count_3+=1
    return count_1,count_2,count_3

def adaptersJoltDiff(data):
    data.sort()
    jolt_1_diff=0
    jolt_2_diff=0
    jolt_3_diff=0
    for i,item in enumerate(data):
        if i==0:
            updated_counts=addCount(item,jolt_1_diff,jolt_2_diff,jolt_3_diff)
            jolt_1_diff=updated_counts[0]
            jolt_2_diff=updated_counts[1]
            jolt_3_diff=updated_counts[2]
        else:
            diff=item-data[i-1]
            updated_counts=addCount(diff,jolt_1_diff,jolt_2_diff,jolt_3_diff)
            jolt_1_diff=updated_counts[0]
            jolt_2_diff=updated_counts[1]
            jolt_3_diff=updated_counts[2]

        if i==len(data)-1:
            jolt_3_diff+=1
    return jolt_1_diff,jolt_3_diff


data=get_data("input.txt")
part1=adaptersJoltDiff(data)
print("1-jolt differences:",part1[0],",3-jolt differences:",part1[1])
print(part1[0]*part1[1])



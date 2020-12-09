#Instructions:https://adventofcode.com/2020/day/6

import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:

            if line == "\n":
                data.append('\n')
            else:
                data.append(line.strip())
    return data
    
def join_data(data):
    data_joined=[]
    pos=0
    while True:
        try: 
            new_line_index=data.index("\n",pos)
            data_joined.append( [''.join(data[pos:new_line_index])])
            pos=new_line_index+1
        except:
            data_joined.append( [''.join(data[pos:len(data)])])
            break
    return data_joined

def unique_responses(data):
    sum_counts=0
    for group in data:
        group =group[0]
        unique_responses=[]
        for i in range(len(group)):
            if group[i] not in unique_responses:
                unique_responses.append(group[i])
        sum_counts+=len(unique_responses)

    return sum_counts


def join_data_by_group(data):
    data_joined=[]
    pos=0
    while True:
        try: 
            new_line_index=data.index("\n",pos)
            data_joined.append( data[pos:new_line_index])
            pos=new_line_index+1
        except:
            data_joined.append( data[pos:len(data)] )
            break
    return data_joined


def group_responses_freq(group):
    group_responses={}
    for i in range(len(group)):
        for j in range(len(group[i])):
            try:
                group_responses[group[i][j]]+=1
            except:
                group_responses[group[i][j]]=1
    return group_responses

def all_group_answers(data):
    sum_counts=0
    for group in data:
        group_responses=group_responses_freq(group)
        people_in_group=len(group)
        for key, value in group_responses.items():
            if value==people_in_group:
                sum_counts+=1
    return sum_counts



data=join_data(get_data('input.txt'))
print("Count the number of questions to which everyone answered - yes: ",unique_responses(data))
data_part2=join_data_by_group(get_data('input.txt'))
print("Count the number of questions to which everyone answered - yes:",all_group_answers(data_part2))
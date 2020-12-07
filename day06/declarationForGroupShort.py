#Instructions:https://adventofcode.com/2020/day/6

import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        data = filehandle.read()
    data=data.split('\n\n')
    return data

def unique_responses(data):
    sum_counts=0
    for group in data:
        unique_responses=set()
        for i in group.split():
            unique_responses.update(i)
        sum_counts+=len(unique_responses)
    return sum_counts

def all_group_answers(data):
    sum_counts=0
    for group in data:
        unique_responses=set(group.split()[0])
        for answers in group.split():
            unique_responses= unique_responses.intersection(answers)
        sum_counts+=len(unique_responses)
    return sum_counts



data=get_data('input.txt')
print("Count the number of questions to which everyone answered - yes: ",unique_responses(data))
print("Count the number of questions to which everyone answered - yes:",all_group_answers(data))


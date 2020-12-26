#Instructions:https://adventofcode.com/2020/day/18
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( (line.rstrip()) )
    return data

def calculate_from_list(lst):
    total=0
    for i,item in enumerate(lst):
        if i==0:
            total=int(item)
        else :
            try:            
                num=int(item)
                operation=lst[i-1]
                if operation=='+':
                    total=total+num
                elif operation=='*':
                    total=total*num
            except:
                continue
    return total

    
def next_brackets(lst):
    left_brack=[]
    right_brack=[]
    for i,item in enumerate(lst):
        if item=="(":
            left_brack.append(i)
        elif item==")":
            right_brack.append(i)
    return left_brack,right_brack


def calculate_brakets(lst):
    if len(next_brackets(lst)[0])==1 and len(next_brackets(lst)[1])==1:
        pos_start=max(next_brackets(lst)[0])
        pos_end=max(next_brackets(lst)[1])
    else:
        pos_start=max(next_brackets(lst)[0])
        min_diff=max(next_brackets(lst)[1])-pos_start
        pos_end=0
        for e in next_brackets(lst)[1]:
            if e-pos_start<=min_diff and e-pos_start>0:
                pos_end=e
                min_diff=e-pos_start

    inside_brackets=lst[pos_start+1:pos_end]
    sum_inside=calculate_from_list(inside_brackets)
    new_lst=lst[:pos_start]+[str(sum_inside)]+lst[pos_end+1:]

    return new_lst

def sum_entry(entry):
    count_brakets=entry.count('(')
    entry=entry.replace("(","( ").replace(")", " )")
    lst=entry.split(' ')
    n=0
    while n<count_brakets:
        lst= calculate_brakets(lst)
        n+=1
    sum_inside=calculate_from_list(lst)
    return sum_inside


def part1_answer():
    total_sum=0
    for line in data:
        result=sum_entry(line)
        total_sum+=result

    print("Part 1 answer: ",total_sum)



data=get_data("input.txt")

part1_answer()


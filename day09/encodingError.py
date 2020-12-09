#Instructions:https://adventofcode.com/2020/day/9
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]

    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( int(line.rstrip()) )
    return data


def isSumOfTwo(data,target,order_of_target,jump):
    isSum=0
    for i,first_number in enumerate(data[order_of_target-jump:order_of_target]):    
        for j,second_number in enumerate(data[order_of_target-jump:order_of_target]):
            sum_of_two=first_number+second_number
            if i!=j and sum_of_two==target:
                isSum=1
    return isSum


def findEncError(data,jump):
    for i,entry in enumerate(data[jump:]):
        sumOfTwo=isSumOfTwo(data,entry,i+jump,jump)
        if sumOfTwo==0:
            print("Number",entry,"is not sum of two previous numbers")
            break

data=get_data("input.txt")       
findEncError(data,25)
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


def is_sum_of_two(data,target,order_of_target,jump):
    isSum=0
    for i,first_number in enumerate(data[order_of_target-jump:order_of_target]):    
        for j,second_number in enumerate(data[order_of_target-jump:order_of_target]):
            sum_of_two=first_number+second_number
            if i!=j and sum_of_two==target:
                isSum=1
    return isSum


def find_enc_error(data,jump):
    encError=0
    for i,entry in enumerate(data[jump:]):
        sumOfTwo=is_sum_of_two(data,entry,i+jump,jump)
        if sumOfTwo==0:
            print("Number",entry,"is not sum of two previous numbers")
            encError=entry
            break
    return encError


def find_encryp_weakness(data):
    i=0
    while i<len(data):   
        sum_of_set=0
        min_number=target
        max_number=0
        for j in data[i:]:
            sum_of_set+=j
            if min_number>j:
                min_number=j
            if max_number<j:
                max_number=j
            if sum_of_set== target and j!=target:
                print("Encoding error found")
                print("Min number is",min_number,",max number is",max_number)
                return min_number+max_number
            if sum_of_set> target:
                break
        i+=1

#Test
data=get_data("test.txt")       
target=find_enc_error(data,5)
print("Encryption weakness in your XMAS-encrypted list of numbers",find_encryp_weakness(data))

#Part 1 and Part2
data=get_data("input.txt")       
target=find_enc_error(data,25)
print("Encryption weakness in your XMAS-encrypted list of numbers",find_encryp_weakness(data))
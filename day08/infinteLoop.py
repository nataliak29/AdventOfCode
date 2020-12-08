import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( [line.rstrip()[:3],int(line.rstrip()[4:])] )
    return data


def accumulator_second_time_execution(data):
    pos=0
    freq={}
    accumulator=0
    while True: 
        instr=data[pos][0]
        move=data[pos][1]
        try:
            freq[pos]+=1
        except: 
            freq[pos]=1

        if freq.get(pos)>=2:
            break

        if instr=="acc":
            accumulator+=move

        if instr=="jmp":
            pos+=move
        else:
            pos+=1
    return accumulator


data=get_data("input.txt")
print("Immediately before any instruction is executed a second time, what value is in the accumulator:",accumulator_second_time_execution(data))





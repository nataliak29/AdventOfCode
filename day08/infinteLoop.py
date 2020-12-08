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
    inf_loop=0
    while True: 
        if pos>=len(data):
            break
        
        instr=data[pos][0]
        move=data[pos][1]
        try:
            freq[pos]+=1
        except: 
            freq[pos]=1

        if freq.get(pos)>=2:
            inf_loop=1
            break

        if instr=="acc":
            accumulator+=move

        if instr=="jmp":
            pos+=move
        else:
            pos+=1
    return accumulator,inf_loop


def switch_instructions(instr_from,instr_to,data):
    for n, i in enumerate(data):
        if i[0] == instr_from:
            data[n][0] = instr_to
            if accumulator_second_time_execution(data)[1]==0:
                print("Accumulator:",accumulator_second_time_execution(data)[0])
                break
            data[n][0] = instr_from



data=get_data("input.txt")
print("Immediately before any instruction is executed a second time, what value is in the accumulator:",accumulator_second_time_execution(data)[0])
switch_instructions("nop","jmp",data)
switch_instructions("jmp","nop",data)


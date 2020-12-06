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


data=get_data('input.txt')
data=join_data(data)
print("Count the number of questions to which everyone answered - yes: ",unique_responses(data))
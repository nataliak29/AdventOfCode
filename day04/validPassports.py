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
            data_joined.append( [' '.join(data[pos:new_line_index])])
            pos=new_line_index+1
        except:
            data_joined.append( [' '.join(data[pos:len(data)])])
            break
    return data_joined

def is_valid_passp(passport_entry):
    passp_req=['ecl:','pid:','eyr:','hcl:','byr:','iyr:','hgt']
    req_count=0
    for j in passp_req:
        if j in passport_entry:
            req_count+=1
        else:
            continue
    if req_count==7:
        return 1

    else:
        return 0


data=get_data('input.txt')
data_joined=join_data(data)
count_valid_passports=0
for i in range(len(data_joined)):
    passport_entry=[]
    passport_entry=data_joined[i][0]
    count_valid_passports+=is_valid_passp(passport_entry)
   
print('Total count of valid passports',count_valid_passports)
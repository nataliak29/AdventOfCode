import os
import re
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

def is_valid_passp_advanced(passport_entry):
    req_count=0
    for item in passport_entry.split(' '):
        item.split(':')
        req=item.split(':')[0]
        req_value=item.split(':')[1]

        if req =='byr':
            if int(req_value)>=1920 and int(req_value)<=2002:
                req_count+=1
        
        if req =='iyr':
            if int(req_value)>=2010 and int(req_value)<=2020:
                req_count+=1
        
        if req =='eyr':
            if int(req_value)>=2020 and int(req_value)<=2030:
                req_count+=1

        if req =='hgt':
            if 'cm' in req_value:
                height = int(re.findall(r'\d+', req_value)[0])
                if height >=150 and height<=193:
                    req_count+=1
            elif 'in' in req_value:
                height = int(re.findall(r'\d+', req_value)[0])
                if height >=59 and height<=76:
                    req_count+=1

        if req =='hcl':
            if req_value[0]=="#":
                if req_value[1:].isalnum()==True and len(req_value[1:])==6:
                    req_count+=1

        if req =='ecl':
            if req_value in ['amb','blu','brn', 'gry', 'grn', 'hzl', 'oth']:
                req_count+=1

        if req =='pid':
            if req_value.isnumeric()==True and len(req_value)==9:
                req_count+=1

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
    count_valid_passports+=is_valid_passp_advanced(passport_entry)
   
print('Total count of valid passports',count_valid_passports)
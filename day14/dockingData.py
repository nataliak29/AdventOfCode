#Instructions:https://adventofcode.com/2020/day/14

import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            text=line.rstrip()
            if text[:4]=="mask":
                d={}
                d[text.split(" = ")[0]]=text.split(" = ")[1]
                data.append(d)
            if text[:3]=="mem":
                d={}
                mem_part=text.split(" = ")[0]
                mem_loc=int(mem_part.split('[')[1][:-1])
                binary_num=bin(int(text.split(" = ")[1]))[2:]
                if len(binary_num)<36:
                    d[mem_loc]='0'*(36-len(binary_num))+binary_num
                data.append(d)
    return data

def apply_mask(data):
    chg_to_1=[]
    chg_to_0=[]
    dict_after_mask={}
    for item in data:
        instr=list(item.keys())[0]
        if instr=="mask":
            chg_to_1=[]
            chg_to_0=[]
            mask=item["mask"]
            for i,element in enumerate(mask):
                if element=="0":
                    chg_to_0.append(i)
                if element=="1":
                    chg_to_1.append(i)
        if instr!="mask":
            val=item[instr]
            for pos in chg_to_0:
                val=val[:pos]+'0'+val[pos+1:]
            for pos in chg_to_1:
                val=val[:pos]+'1'+val[pos+1:]
            dict_after_mask[instr]=int(val,2)
    return dict_after_mask

def final_sum(dict_after_mask):
    final_sum=0
    for k,v in dict_after_mask.items():
        final_sum+=v
    return final_sum


#data=get_data("test.txt")
data=get_data("input.txt")
dict_after_mask=apply_mask(data)
print("Part 1 Answer:",final_sum(dict_after_mask))






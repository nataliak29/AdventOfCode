#Instructions:https://adventofcode.com/2020/day/7

import os
import re
def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        data = filehandle.read()
    data=data.split('\n')
    return data


def parse_rules(data):
    rules_bags={}
    for rule in data:
        if rule =="":
            continue

        bags=[]
        main_bag=rule.split('bags contain')[0].strip()
        bags_inside=rule.split('bags contain')[1]
        result = re.split(",", bags_inside)

        for i in result:        
            s = re.sub(r'[^\w\s]','',i).replace("bags", "").replace("bag", "").replace(" other","").strip()
            if s==" " or s=="" or s[0]=="n":
                continue
            else:
                bags.append((int(s[0]),s[1:].strip()))
    
        rules_bags[main_bag]=bags
    return rules_bags
    

data=get_data("input.txt")
rules_bags=parse_rules(data)

def find_parents(rules_bags,child_bag):
    parents_count=0
    parents=set()
    while True:
        for parent in rules_bags:
            for child in rules_bags[parent]:
                if child[1]==child_bag or child[1] in parents:
                    parents.add(parent)
        if len(parents)>parents_count:
            parents_count=len(parents)
     
        else:
            break
    return parents

parents=find_parents(rules_bags,"shiny gold")
print("Number of bag colors that can eventually contain at least one shiny gold bag:",len(parents))










# key="light red"
# count=0
# i=0
# while i<20:
#     print("key",key)
#     value=rules_bags.get(key)
#     for bag in value:
#         key=bag
#         print("bag",bag)
#         if bag=="shiny gold":
#             print("shiny gold found!!!")
#             count+=1
#             break
#         elif bag=="no":
#             break


# count=0
# for key,value in rules_bags.items(): 
#     print("key:",key)
#     for bag in value:
#         print("bag in value:",bag)
#         new_value=""
#         while new_value!='no':
#             new_key=bag
#             new_value=rules_bags.get(new_key)
#             print("new value",new_value)
#         count+=1


# freq={}
# for key,value in rules_bags.items(): 
#     print("key:",key)
#     for bag in value:
#         print("bag:",bag)
#         try:
#             freq[bag]=freq.get(bag) +1
#         except:
#             freq[bag]=1
# print(freq)

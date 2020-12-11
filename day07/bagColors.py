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
    

#data=get_data("test.txt")
#rules_bags=parse_rules(data)
#print(rules_bags)
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


def bag_contains(target,bag):
   
    if  bag==None or len(bag)==0: #if no children are found return false
        return False
    for key in bag:     
        if key[1]==target: #check if bag contain target and return true
            return True 
    for key in bag:       
        if bag_contains(target,data.get(key[1])) == True: #else look up bagContains for every child
            return True
    return False


def count_parents(data,target):
    parents_count=0
    for key,bag in data.items():
        if bag_contains(target,bag)==True:
            parents_count+=1
    return parents_count

#data={'shiny gold': [(10, 'dark olive'), (2, 'vibrant plum')], 'dark olive': [(3, 'faded blue'), (4, 'dotted black')]}
#bag=[(1, 'dark olive'), (2, 'vibrant plum')]

    
def bag_children(target):
  count = 0
  children=data.get(target)
  if children==None:
      return count
  
  for bag in children:
      #print("bag",bag,"count start",count)
      count += bag[0] + bag[0] * bag_children(bag[1])
      #print("count end",count)

  return count

target="shiny gold"
data=parse_rules(get_data("input.txt"))
print(count_parents(data,"shiny gold"),"bag colors can eventually contain at least one shiny gold bag")

print("answer:",bag_children(target))


    



#Instructions:https://adventofcode.com/2020/day/16
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( (line.rstrip()) )
           
        rules=data[:data.index('')]
        your_ticket=data[data.index('your ticket:')+1:data.index('your ticket:')+2]
        nearby_tickets=data[data.index('nearby tickets:')+1:]
    return rules,your_ticket,nearby_tickets

def parse_rules(rules):
    rules_dict={}
    for rule in rules:
        inst=rule.split(':')[0]
        values=rule.split(': ')[1]
        order=1        
        for val in values.split(' or '):
            values_lst=[]
            values_lst.append(int(val.split('-')[0]))
            values_lst.append(int(val.split('-')[1]))
            rules_dict[inst+str(order)]=values_lst
            order+=1
    return rules_dict

def parse_nearby_tickets(raw_tickets):
    parsed_tickets=[]
    for ticket in raw_tickets:
        parsed_ticket=[]
        items=ticket.split(',')
        for i in items:
            parsed_ticket.append(int(i))
        parsed_tickets.append(parsed_ticket)
    return parsed_tickets

def ticket_invalid_entry(tick_entry):
    for key in rules:
        min_k=rules[key][0]
        max_k=rules[key][1]
        if tick_entry<=max_k and tick_entry>=min_k:
            return True
    return False

def check_tickets(nearby_tickets):
    err_rate=0
    for ticket in nearby_tickets:
        for entry in ticket:
            if ticket_invalid_entry(entry)==False:
                err_rate+=entry
    return err_rate


def valid_tickets(nearby_tickets):
    invalid_tickets=[]
    valid_tickets_list=[]
    for ticket in nearby_tickets:
        for entry in ticket:
            if ticket_invalid_entry(entry)==False:
                invalid_tickets.append(ticket)
    valid_tickets_list= [x for x in nearby_tickets if x not in invalid_tickets]
            
    return valid_tickets_list

def find_entry_name(col_num):
    name_dict={}
    for tick in valid_nearby_tickets:
        tick_entry=tick[col_num]

        for key in rules:        
            min_k=rules[key][0]
            max_k=rules[key][1]
            if tick_entry<=max_k and tick_entry>=min_k:
                try:
                    name_dict[key[:-1]]= name_dict.get(key[:-1])+1
                except:
                    name_dict[key[:-1]]=1
    return name_dict




rules_raw,raw_your_ticket,raw_nearby_tickets=get_data("input.txt")
rules= parse_rules(rules_raw)
nearby_tickets=parse_nearby_tickets(raw_nearby_tickets)
your_ticket=parse_nearby_tickets(raw_your_ticket)
print("Part 1 answer:",check_tickets(nearby_tickets))

valid_nearby_tickets=valid_tickets(nearby_tickets)
len_rules=len(rules)/2


def decode_tickets():
    final_dict={}
    for col in range(len(your_ticket[0])):
        name_dict=find_entry_name(col)
        d=[]
        for k in name_dict:
            if name_dict[k]==len(valid_nearby_tickets):
                d.append(k)
        final_dict[col]=d
    
    found=[]
    d={}
    i=0
    while  i<len_rules:
    
        for k in final_dict:
            if len(final_dict[k])==1:
                found.append(final_dict[k][0])
                d[k]=final_dict[k][0]
    
        for k in final_dict:
            this_d=final_dict[k]
            this_d_n= [x for x in this_d if x not in found]
            final_dict[k]=this_d_n
        i+=1
    return d

decoded=decode_tickets()
final_product=1
for k,v in decoded.items():
    if decoded[k][:9]=="departure":
        final_product=final_product*your_ticket[0][k]

print("Part 2 answer:",final_product)



           

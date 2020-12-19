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
        #print(inst,values)
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


rules_raw,raw_your_ticket,raw_nearby_tickets=get_data("input.txt")
rules= parse_rules(rules_raw)
nearby_tickets=parse_nearby_tickets(raw_nearby_tickets)
your_ticket=parse_nearby_tickets(raw_your_ticket)

print("Part 1 answer:",check_tickets(nearby_tickets))

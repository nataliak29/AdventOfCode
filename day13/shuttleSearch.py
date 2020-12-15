#Instructions:https://adventofcode.com/2020/day/13
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]

    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( (line.rstrip()) )
    return data


def next_buses_dict(data,start_time):
    buses=data[1].split(",")
    when_is_next_bus=0
    diff=0
    next_buses={}
    for bus in buses:
        if bus!="x":
            bus=int(bus)
            when_is_next_bus=bus*round(start_time/bus,0)
            diff=when_is_next_bus-start_time
            if diff<0:
                when_is_next_bus=when_is_next_bus+bus
                diff=when_is_next_bus-start_time
            next_buses[bus]=[when_is_next_bus,diff]
    return next_buses

data=get_data("test.txt")
start_time=int(data[0])
next_buses=next_buses_dict(data,start_time)
next_bus = min(next_buses.keys(), key=(lambda k: next_buses[k]))
print("Answer for part 1",next_bus*next_buses[next_bus][1])


#https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/
def find_timest(data):

    buses=data[1].split(",")
    buses_dict={}
    for i,bus in enumerate(buses):
        if bus!='x':
            buses_dict[int(bus)]=i
    #print(buses_dict)
    start, step = 0, 1
    for id, delta in buses_dict.items():
        #print(id,delta)
        for guess in range(start, step * id, step):
            #print("start",start,"step*id",step*id,"step",step)
            #print ("guess",guess)
            if (guess + delta) % id == 0:
                step *= id
                start = guess
                #print("condition satisf",guess)
        if id==list(buses_dict)[-1]:
            return guess
        
     

print("Part 2 answer:",find_timest(data))




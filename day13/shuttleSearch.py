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

data=get_data("input.txt")
start_time=int(data[0])
next_buses=next_buses_dict(data,start_time)
next_bus = min(next_buses.keys(), key=(lambda k: next_buses[k]))
print("Answer for part 1",next_bus*next_buses[next_bus][1])





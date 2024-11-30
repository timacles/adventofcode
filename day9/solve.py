SAMPLE1 = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

from dataclasses import dataclass
from utils import load_input_file, debug


###########################==--
### SOLVING  part 2 #########==--
## ==---------

def solve_part2(input):
    print(f"*** Part 2 ***")
    data = parse(input)
    results = []
    
    #*** *** *** *** ***
    # main loop 
    #*** *** *** *** ***

    for entry in data:
        debug(f"*** Start Value: {entry}")

        # Stages is each "cycle" of values
        # the first stage is the initial set of values
        stages = [entry]

        steps = calc_steps(entry) 
        i = 0 
        while True:
            stages.append(steps)
            i += 1
            #debug(f"  {i} - {steps}")
            steps = calc_steps(steps)
            if all(s==0 for s in steps):
                break

        # reverse to start from the bottom
        stages = stages[::-1]
            
        for i, steps in enumerate(stages):
            debug(f"  {i} - {steps}")
            first_step = steps[0]
            try:
                next_first_step = stages[i+1][0] 
            # stop loop if there are no elements left 
            except IndexError:
                break

            ## Append to next stage element
            ## at beginning of list
            result = next_first_step - first_step
            stages[i+1].insert(0, result)

            #debug(f"     - First step: {first_step} ; next first step {next_first_step}")

        # first value of the last "stage" element
        result = stages[-1][0]
        debug(f"    Result: {result}")
        results.append(result)
    return sum(results)


###########################==--
### SOLVING part 1 #########==--
## ==---------

def solve_part1(input):
    print(f"*** Part 1")
    data = parse(input)
    results = []
    ##########
    ### Start main loop over data
    ##
    for entry in data:
        debug(f"Start Value: {entry}")

        # First loop determines each lower stage
        # store initial value
        stages = [entry]
        steps = calc_steps(entry) 
        i = 0 
        while True:
            stages.append(steps)
            i += 1
            #debug(f"  {i} - {steps}")
            steps = calc_steps(steps)
            if all(s==0 for s in steps):
                break
            

        # Second loop iterate backwards over 
        # each stage adding the last value previous stage
        stages = stages[::-1]
        for i, steps in enumerate(stages):
            debug(f"  {i} - {steps}")
            last_val = steps[-1]
            try:
                # Get last val of the next stage
                last_val_next =  stages[i+1][-1]
                stages[i+1].append(last_val + last_val_next)
            # end of list
            except IndexError:
                break
        # since we reversed the list, the "next" value
        # is the last value of the last stage entry
        results.append(stages[-1][-1])

    return sum(results)


###########################
### functions
##

def calc_steps(entry):
    steps = []
    for i in range(1, len(entry)):
        step = entry[i] - entry[i-1]
        steps.append(step)
    return steps

def parse(input):
    data = []
    for line in input.split('\n'):
        if line == '': continue
        entry = [int(i) for i in line.split(' ')]
        data.append(entry)
        #data.append(Entry(entry))
    return data 

@dataclass
class Entry:
    data: list
    steps: list = None

    


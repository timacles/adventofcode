SAMPLE = "sample.txt"
INPUT = "input.txt"
RE_PTRN1 = "\W+"


from re import split as re_split
from math import prod

def main():
    raw = load_file(INPUT)
    time, dist = parse_raw(raw)
    results = process(time, dist)
    product = prod(results)
    print()
    print("******")
    print("product:",product)

def process(time, dist):
    results = [] 
    for i in range(len(time)):
        t = time[i]
        d = dist[i]
        result = calc(t, d)
        results.append(result)
    #print("Results:", results)
    return results
    
def calc(time, dist):
    time = int(time)
    dist = int(dist) 
    count = 0
    for i in range(1, time):
       remaining = time - i
       x = remaining * i
       if x > dist:
           count += 1
    return count

def sanitize(elems):
    clean = []
    for e in elems:
        if is_bad(e):
            continue
        clean.append(e)
    return clean 

def join_elements(elements):
    out = ""
    for x in elements:
        out += x
    return [out]

def is_bad(elem):
    if elem == "":
        return True
    elif elem in ["Time", "Distance"]:
        return True
    return False 

def parse_raw(data):
    time, dist = list(map(lambda text: re_split(RE_PTRN1, text), data))
    return sanitize(time), sanitize(dist)

def load_file(f):
    with open(f) as f:
        data = f.readlines()
    return data

if __name__ == "__main__":
    main()

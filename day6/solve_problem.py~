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
    # loop over each element
    for i in range(1, len(time)):
        t = time[i]
        d = dist[i]
        if t == "": continue

        print("  time:", time[i], "dist:", dist[i])

        count = calc(t, d)
        results.append(count)
    print("Results:", results)
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
           #print("  i:", i, "calc:", x)
    return count
    
def parse_raw(data):
    return list(map(lambda text: re_split(RE_PTRN1, text), data))

def parse_partial(time, dist):
    return time, dist

def load_file(f):
    with open(f) as f:
        data = f.readlines()
    return data

if __name__ == "__main__":
    main()

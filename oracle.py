import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def cents(x):
    return math.floor(x * 100 + 0.5) / 100

def fixed1(x):
    return f"{tenths(x):.1f}"

def money(x):
    return f"{cents(x):.2f}"

def load_truth(people, capacity):
    if not (people > 0):
        raise ValueError("the people must be above zero")
    if not (capacity > 0):
        raise ValueError("the capacity must be above zero")
    pieces = people * 6
    days = capacity / pieces
    makes = "makes" if people == 1 else "make"
    return f"{people} {plural(people, 'person', 'people')} {makes} {pieces} pieces a day; a {capacity}-piece washer fills in {fixed1(days)} {plural(tenths(days), 'day', 'days')} honestly."

def half_truth(half_loads, gallons):
    if not (half_loads >= 0):
        raise ValueError("the half-loads must be zero or more")
    if not (gallons > 0):
        raise ValueError("the gallons per load must be above zero")
    if half_loads == 0:
        return "0 half-loads a week wastes nothing honestly."
    waste = half_loads * gallons * 52
    runs = "runs" if half_loads == 1 else "run"
    return f"{half_loads} half-{plural(half_loads, 'load', 'loads')} a week at {gallons} gallons each {runs} {fixed1(waste)} extra gallons a year honestly."

def pod_truth(loads, cost):
    if not (loads > 0):
        raise ValueError("the loads must be above zero")
    if not (cost > 0):
        raise ValueError("the pod cost must be above zero")
    pods = loads * 52
    return f"{loads} {plural(loads, 'load', 'loads')} a week is {fixed1(pods)} pods a year - at ${money(cost)} each, ${money(pods * cost)} honestly."

FNS = {"loadTruth": load_truth, "halfTruth": half_truth, "podTruth": pod_truth}

CASES = [
    ("loadTruth", [4, 120]),
    ("loadTruth", [1, 120]),
    ("loadTruth", [2, 100]),
    ("loadTruth", [6, 140]),
    ("loadTruth", [3, 120]),
    ("loadTruth", [20, 120]),
    ("loadTruth", [0, 120]),
    ("loadTruth", [4, 0]),
    ("halfTruth", [3, 4]),
    ("halfTruth", [1, 4]),
    ("halfTruth", [7, 3.5]),
    ("halfTruth", [2, 5]),
    ("halfTruth", [0, 4]),
    ("halfTruth", [0.5, 4]),
    ("halfTruth", [-1, 4]),
    ("halfTruth", [3, 0]),
    ("podTruth", [5, 0.25]),
    ("podTruth", [7, 0.30]),
    ("podTruth", [3, 0.2]),
    ("podTruth", [1, 0.25]),
    ("podTruth", [4, 0.35]),
    ("podTruth", [0, 0.25]),
    ("podTruth", [5, 0]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")

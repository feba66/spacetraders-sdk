from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

WORTH = {
    "ICE_WATER":14,
    "QUARTZ_SAND":19,
    "SILICON_CRYSTALS":34,
    "AMMONIA_ICE":39,
    "IRON_ORE":44,
    "ALUMINUM_ORE":49,
    "COPPER_ORE":54,
    "SILVER_ORE":59,
    "GOLD_ORE":64,
    "PLATINUM_ORE":69,
    "DIAMONDS":3946,
}

def determine_worth(materials:list[str]):
    w = 0
    for m in materials:
        if m not in WORTH:
            print("No price set for "+ m)
        else:
            w+=WORTH[m]
    return w/len(materials)

# with open("surveys_v1.csv","r") as f:
#     line = f.readlines()

d = defaultdict(lambda: 0)
size = defaultdict(lambda:0)
duration = defaultdict(lambda:[])
mw = 0
# for l in line:
#     s = l.replace("\n","").split(";")[4:]
#     size[l.replace("\n","").split(";")[1]]+=1
#     for ressource in s:
#         d[ressource]+=1
#     w = determine_worth(s)
#     if w > mw:
#         print(f"Worth: {w}  {s}")
#         mw=w

with open("surveys.csv","r") as f:
    line = f.readlines()

for l in line:
    spl = l.replace("\n","").split(";")
    s = spl[5:]
    size[spl[1]]+=1
    duration[spl[1]].append((spl[1],float(spl[3])))
    for ressource in s:
        d[ressource]+=1
    # w = determine_worth(s)
    # if w > mw:
    #     print(f"Worth: {w}  {s}")
    #     mw=w
if "EXHAUSTED" in d:
    del d["EXHAUSTED"]
# ld = list(size.items())
ld = list(d.items())
ld.sort(key=lambda x : x[1])

pprint(ld)
# pprint(ships)

fig,ax = plt.subplots()
# ax.bar(d.keys(),d.values())
ax.bar([x[0] for x in ld],[x[1] for x in ld])
# ax.bxp(ship_data,showfliers=False)
# i=0
# for du in duration:
#     i+=1
#     ax.scatter([i]*len(duration[du]),[x[1]/60 for x in duration[du]],label=du)

# ax.legend()

# ax.set_title("Survey Size time to Expire")
# ax.set_ylabel("Expire time in min")
# ax.set_xticks([1,2,3])
# ax.set_xticklabels(duration.keys())
# ax.set_title("Survey Material Occurences")
ax.set_title("Survey Sizes")
ax.set_ylabel("Count")
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
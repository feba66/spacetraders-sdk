from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open("extractions.csv","r") as f:
    line = f.readlines()
d,surv = defaultdict(lambda: 0),defaultdict(lambda: [])
ships = defaultdict(lambda:[])
for l in line:
    s = l.replace("\n","").split(";")
    if s[0]=="None":
        d[s[2]]+=1
        ships[s[1]].append(int(s[3]))
    else:
        surv[s[1]].append(int(s[3]))



ld = list(d.items())
ld.sort(key=lambda x : x[1])
pprint(ld)

# pprint(ships)

ship_data = []
for s in ships:
    ship_data.append({"whislo": min(ships[s]),
                      "whishi":max(ships[s]),
                      "med":np.percentile(ships[s],50),
                      "q1":np.percentile(ships[s],25),
                      "q3":np.percentile(ships[s],75),
                      "label":s+" No"})
for s in surv:
    ship_data.append({"whislo": min(surv[s]),
                      "whishi":max(surv[s]),
                      "med":np.percentile(surv[s],50),
                      "q1":np.percentile(surv[s],25),
                      "q3":np.percentile(surv[s],75),
                      "label":s +" With"})

fig,ax = plt.subplots()
# ax.bar(d.keys(),d.values())

ax.bxp(ship_data,showfliers=False)
ax.set_title("Extraction Amount per Ship at X1-DF55-17335A")

# ax.bar([x[0] for x in ld],[x[1] for x in ld])
# ax.set_title("Default Extraction Material Occurences at X1-DF55-17335A")

ax.set_ylabel("Count")

fig.autofmt_xdate()
plt.tight_layout()
plt.show()
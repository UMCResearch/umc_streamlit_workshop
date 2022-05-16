"""
This file is used to generate fake, VAERS-Like data for demonstration purposes only.
"""

import re
import random
from collections import defaultdict
from datetime import datetime, timedelta

import pandas as pd
from datasets import load_dataset

random.seed(42)

dataset = load_dataset('newsgroup', 'bydate_sci.med')

data = defaultdict(list)
id = 30234

def clean(txt):
    line_finder = re.search(r"Lines: \d+", txt)
    
    if line_finder is not None:
        txt = txt[line_finder.end():].strip()

    return txt.replace("\n", " ")

for train_example in dataset['train']:
    text = clean(train_example["text"])

    data["VAERS_ID"].append(id)
    data["SYMPTOM_TEXT"].append(text[0:400])

    id = id + 1

k = len(data["VAERS_ID"])

data["SEX"] = random.choices(["M", "F", "U"], weights=[0.65, 0.27, 0.08], k=k)
data["NUMDAYS"] = [int(random.expovariate(1 / 26)) for _ in range(k)]

start_date = datetime(2020, 1, 1)
data["RECVDATE"] = [start_date + timedelta(days=int(random.expovariate(-1 / 200))) for _ in range(k)]

pd.DataFrame(data).to_csv("../2020VAERSLike.csv", encoding="cp1252", index=False)
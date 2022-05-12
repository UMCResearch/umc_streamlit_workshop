"""
This file is used to generate fake, VAERS-Like data for demonstration purposes only.
"""

import random
from collections import defaultdict
from datetime import datetime, timedelta

import pandas as pd
from datasets import load_dataset

random.seed(42)

dataset = load_dataset('newsgroup', 'bydate_sci.med')

data = defaultdict(list)
id = 30234

for train_example in dataset['train']:
    data["VAERS_ID"].append(id)
    data["SYMPTOM_TEXT"].append(train_example["text"].replace("\n", " "))

    id = id + 1

k = len(data["VAERS_ID"])

data["SEX"] = random.choices(["M", "F", "U"], weights=[0.65, 0.27, 0.08], k=k)
data["NUMDAYS"] = [int(random.expovariate(1 / 26)) for _ in range(k)]

start_date = datetime(2020, 1, 1)
data["RECVDATE"] = [start_date + timedelta(days=int(random.expovariate(-1 / 200))) for _ in range(k)]

pd.DataFrame(data).to_csv("2020VAERSLike.csv", encoding="cp1252", index=False)
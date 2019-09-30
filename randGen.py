import json
import random

# q1 Gender
q1a = random.randint(1, 2)

# sub q1 pregnant
if q1a == 2:
    q1b = random.randint(0, 1)
else:
    q1b = 0

# q2 Race/Ethnicity
q2 = random.randint(1, 6)

# q3 Personal Health History
q3a = random.randint(0, 1)
q3b = random.randint(0, 1)
q3c = random.randint(0, 1)
q3d = random.randint(0, 1)
q3e = random.randint(0, 1)
q3f = random.randint(0, 1)
q3g = random.randint(0, 1)
q3h = random.randint(0, 1)
q3i = random.randint(0, 1)
q3j = random.randint(0, 1)
q3k = random.randint(0, 1)

# q4 Overall Health
q4 = random.randint(1, 5)

# q5 preventative health tests
q5a = random.randint(1, 2)
q5b = random.randint(1, 2)
q5c = random.randint(1, 2)
q5d = random.randint(1, 2)
q5e = random.randint(1, 2)
q5f = random.randint(1, 2)
q5g = random.randint(1, 2)
q5h = random.randint(1, 2)
q5i = random.randint(1, 2)
q5j = random.randint(1, 2)

# q6 Common health tests
q6a = random.randint(1, 4)
q6b = random.randint(1, 4)
q6c = random.randint(1, 4)

# q7 Medications
q7a = random.randint(0, 1)
q7b = random.randint(0, 1)
q7c = random.randint(0, 1)

# create tuple for output
qTuple = {"q1a": q1a,
          "q1b": q1b,
          "q2": q2,
          "q3a": q3a,
          "q3b": q3b,
          "q3c": q3c,
          "q3d": q3d,
          "q3e": q3e,
          "q3f": q3f,
          "q3g": q3g,
          "q3h": q3h,
          "q3i": q3i,
          "q3j": q3j,
          "q3k": q3k,
          "q4": q4,
          "q5a": q5a,
          "q5b": q5b,
          "q5c": q5c,
          "q5d": q5d,
          "q5e": q5e,
          "q5f": q5f,
          "q5g": q5g,
          "q5h": q5h,
          "q5i": q5i,
          "q5j": q5j,
          "q6a": q6a,
          "q6b": q6b,
          "q6c": q6c,
          "q7a": q7a,
          "q7b": q7b,
          "q7c": q7c
          }

with open('digitalWellness.json', 'w') as outFile:
    json.dump(qTuple, outFile, indent=2)

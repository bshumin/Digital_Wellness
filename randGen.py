import json
import random

# output file name
fName = 'randGen.json'

# desired number of fake patient data
patients = 100

# create empty list in the json file
with open(fName, mode='w', encoding='utf-8') as f:
    json.dump([], f)

# generate given number of pseudo-random patient data
for i in range(patients):

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

    # q8 Sick Days
    q8 = random.randint(0, 9)

    # q9 Exercise days
    q9 = random.randint(0, 7)

    # q10 Strength Exercise
    q10 = random.randint(0, 3)

    # q11 stretching exercise
    q11 = random.randint(0, 3)

    # q12 breakfast
    q12 = random.randint(1, 3)

    # q13 whole grains
    q13 = random.randint(0, 6)

    # q14 Fruits
    q14 = random.randint(0, 8)

    # q15 Vegetables
    q15 = random.randint(0, 8)

    # q16 Protein
    q16 = random.randint(0, 6)

    # q17 Kind of proteins
    q17 = random.randint(1, 3)

    # q18 Fats
    q18 = random.randint(1, 3)

    # q19 dairy
    q19 = random.randint(0, 6)

    # q20 Nuts/Seeds
    q20 = random.randint(0, 6)

    # q21 sweets
    q21 = random.randint(0, 5)

    # q22 water
    q22 = random.randint(0, 7)

    # q23 salt
    q23 = random.randint(1, 3)

    # q24 supplements
    q24a = random.randint(0, 1)  # Calcium
    q24b = random.randint(0, 1)  # Vitamin D
    q24c = random.randint(0, 1)  # Vitamin B12
    q24d = random.randint(0, 1)  # multivitamin/mineral

    # q25 smoking status
    q25 = random.randint(1, 3)

    # q26 secondhand smoke
    q26 = random.randint(1, 2)

    # q27 alcohol
    q27 = random.randint(0, 5)

    # q28 drugs
    q28 = random.randint(1, 3)

    # q29 kinds of drugs
    q29 = random.randint(0, 8)

    # q30 stress at work
    q30 = random.randint(1, 4)

    # q31 stress at home
    q31 = random.randint(1, 4)

    # q32 stress from finance
    q32 = random.randint(1, 3)

    # q33 traumatic life experiences
    q33 = random.randint(0, 3)

    # q34 Outlook
    q34 = random.randint(1, 3)

    # q35 control
    q35 = random.randint(1, 4)

    # q36 Happiness
    q36 = random.randint(1, 3)

    # q37 Mood
    q37 = random.randint(1, 2)

    # q38 Functioning
    q38 = random.randint(1, 2)

    # q39 Relax
    q39 = random.randint(1, 3)

    # q40 energy
    q40 = random.randint(1, 3)

    # q41 satisfaction
    q41 = random.randint(1, 4)

    # q42 social support
    q42a = random.randint(0, 1)  # married/significant other
    q42b = random.randint(0, 1)  # frequent contact with family and friends
    q42c = random.randint(0, 1)  # participate in faith group
    q42d = random.randint(0, 1)  # participate in social group

    # q43 sleep
    q43 = random.randint(1, 4)

    # q44 seat belts
    q44 = random.randint(0, 5)

    # q45 child safety seats
    q45 = random.randint(1, 3)

    # q46 drinking and driving
    q46 = random.randint(0, 8)

    # q47 smoke alarm
    q47 = random.randint(1, 2)

    # q48 driving
    q48 = random.randint(1, 3)

    # q49 Lifting
    q49 = random.randint(1, 3)

    # q50 Sun
    q50 = random.randint(1, 3)

    # q51 Helmets
    q51 = random.randint(1, 3)

    # q52 Optional Question, STD FIXME check for desired behavior of optional question
    q52 = random.randint(1, 3)

    # q53 Work Life
    q53 = random.randint(1, 4)

    # q54 Productivity
    q54 = random.randint(0, 9)

    # q55 Limitations
    q55 = random.randint(0, 3)

    # q56 Health Culture
    q56 = random.randint(1, 4)

    # q57 lifestyle changes
    q57a = random.randint(1, 5)  # physically active
    q57b = random.randint(1, 5)  # practice good eating habits
    q57c = random.randint(1, 5)  # avoid smoking or using tobacco
    q57d = random.randint(1, 5)  # lose weight or maintain a healthy weight
    q57e = random.randint(1, 5)  # cope better with stress
    q57f = random.randint(1, 5)  # lower or maintain healthy cholesterol level
    q57g = random.randint(1, 5)  # lower or maintain healthy blood pressure
    q57h = random.randint(1, 5)  # avoid alcohol or drink in moderation
    q57i = random.randint(1, 5)  # live an overall healthy lifestyle

    # create tuple for output
    qTuple = {"q1a": q1a,
              "q1b": q1b,
              "q2":  q2,
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
              "q7c": q7c,
              "q8": q8,
              "q9": q9,
              "q10": q10,
              "q11": q11,
              "q12": q12,
              "q13": q13,
              "q14": q14,
              "q15": q15,
              "q16": q16,
              "q17": q17,
              "q18": q18,
              "q19": q19,
              "q20": q20,
              "q21": q21,
              "q22": q22,
              "q23": q23,
              "q24a": q24a,
              "q24b": q24b,
              "q24c": q24c,
              "q24d": q24d,
              "q25": q25,
              "q26": q26,
              "q27": q27,
              "q28": q28,
              "q29": q29,
              "q30": q30,
              "q31": q31,
              "q32": q32,
              "q33": q33,
              "q34": q34,
              "q35": q35,
              "q36": q36,
              "q37": q37,
              "q38": q38,
              "q39": q39,
              "q40": q40,
              "q41": q41,
              "q42a": q42a,
              "q42b": q42b,
              "q42c": q42c,
              "q42d": q42d,
              "q43": q43,
              "q44": q44,
              "q45": q45,
              "q46": q46,
              "q47": q47,
              "q48": q48,
              "q49": q49,
              "q50": q50,
              "q51": q51,
              "q52": q52,
              "q53": q53,
              "q54": q54,
              "q55": q55,
              "q56": q56,
              "q57a": q57a,
              "q57b": q57b,
              "q57c": q57c,
              "q57d": q57d,
              "q57e": q57e,
              "q57f": q57f,
              "q57g": q57g,
              "q57h": q57h,
              "q57i": q57i
              }

    # load existing json file
    with open(fName) as feed_json:
        feeds = json.load(feed_json)

    # append new data and save json
    feeds.append(qTuple)
    with open(fName, mode='w') as f:
        f.write(json.dumps(feeds, indent=2))

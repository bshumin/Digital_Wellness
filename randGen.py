import json
import random

# output file name
fName = 'randGen.json'

# seed random generator
random.seed(a=None, version=2)
#               J   F   M   A   M   J   J   A   S   O   N   D
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# desired number of fake patient data
patients = input("Enter Number of Patients to Generate: ")

# create empty list in the json file
with open(fName, mode='w', encoding='utf-8') as f:
    json.dump([], f)

# generate given number of pseudo-random patient data
for i in range(int(patients)):

    # GENERAL QUESTIONS-------------------------------------------------------------------------------------------------
    # in general 1 = yes, 2 = no, -1 = N/A

    # q1 Name
    Name = "Patient #" + str(i+1)

    # q2 Gender
    # 1 male
    # 2 female
    gender = random.randint(1, 2)

    # # sub q2 pregnant
    # if q1a == 2:
    #     q1b = random.randint(1, 2)
    # else:
    #     q1b = 0

    # q3 DOB in MM/DD/YYYY
    temp = random.randint(1, 12)
    yearOfBirth = random.randint(1920, 2002)
    DOB = str(temp) + '/' + str(random.randint(1, daysInMonth[temp - 1])) + '/' + str(yearOfBirth)

    # q4 height in inches
    if gender == 1:
        height = random.randint(58, 82)  # male height within 4 std dev
    else:
        height = random.randint(53, 77)  # female height within 4 std dev

    # q5 weight
    weight = random.randint(120, 230)

    # q6 race/ethnicity
    # 1  White/Caucasian
    # 2  African American
    # 3  Hispanic or Latino
    # 4  Asian
    # 5  Native American
    # 6  Other
    race = random.randint(1, 6)

    # q7 how good is your health
    # 1 Great
    # 2 Good
    # 3 Neutral
    # 4 Bad
    # 5 Terrible
    health = random.randint(1, 5)

    # q8 hours of sleep
    hrSleep = random.randint(5, 12)

    # q9 physical in the last 2 years?
    physical2years = random.randint(1, 2)

    # ANY OF THE FOLLOWING----------------------------------------------------------------------------------------------
    # q10
    # allergies?
    allergies = random.randint(1, 2)
    # TODO what ae you  allergic to?

    # asthma?
    asthma = random.randint(1, 2)
    # arthritis?
    arthritis = random.randint(1, 2)
    # chronic back pain?
    backPain = random.randint(1, 2)
    # chronic lung disease(COPD)?
    COPD = random.randint(1, 2)
    # chronic sinus problems?
    sinusProblems = random.randint(1, 2)
    # heart disease or angina?
    angina = random.randint(1, 2)
    # broken bones or fractures in the last 10 years
    brokenBones = random.randint(1, 2)
    # Have you had heart surgery, like a coronary artery bypass or angioplasty?
    heartSurgery = random.randint(1, 2)

    # Have you had your blood pressure checked in the past 2 years?
    bpCheck = random.randint(1, 2)
    # Was your blood pressure normal or elevated? Normal is less than 120/80.
    # 0-Normal 1-elevated
    normalBP = random.randint(1, 2)
    # Do you take blood pressure medication?
    bpMeds = random.randint(1, 2)

    # Have you had your cholesterol checked in the past 5 years?
    cholesterolCheck = random.randint(1, 2)
    # Was your cholesterol normal or elevated? Normal is less than 200.
    # 0-Normal 1-elevated
    normalCholesterol = random.randint(1, 2)
    # Do you take cholesterol medication?
    cholesterolMeds = random.randint(1, 2)

    cancerHistory = random.randint(1, 2)
    # TODO what kind of cancer
    # age of diagnosis
    if cancerHistory == 1:
        cancerAge = random.randint(0, 2020-yearOfBirth)
    else:
        cancerAge = -1
    # only check for feminine cancer risks if not male
    if gender == 2:
        # Have you had a pap test in the past three years?
        papTest = random.randint(1, 2)

        if papTest == 1:
            # Was your pap test normal or abnormal?
            papTestNormal = random.randint(1, 2)
        else:
            papTestNormal = -1
        # Have you had a mammogram in the past two years?
        mammogram = random.randint(1, 2)

        if mammogram == 1:
            # Was your mammogram normal or abnormal?
            mammogramNormal = random.randint(1, 2)
        else:
            mammogramNormal = -1
    else:  # patient is male
        papTest = -1
        papTestNormal = -1
        mammogram = -1
        mammogramNormal = -1

    # diabetes, or high blood sugar?
    diabetes = random.randint(1, 2)
    # Have you had your blood sugar checked in the past year?
    bloodSugarCheck = random.randint(1, 2)
    # Was your blood sugar normal or elevated? Normal is less than 100.
    normalBloodSugar = random.randint(1, 2)
    # Do you take blood sugar medication, or medication for diabetes?
    diabetesMeds = random.randint(1, 2)
    # stroke, or restricted blood flow to your head or legs?
    stroke = random.randint(1, 2)

    # q11 Any other medication
    otherMeds = random.randint(1, 2)
    # q12
    overCounterMeds = random.randint(1, 2)
    # q13 Any supplements
    supplements = random.randint(1, 2)
    # TODO add clarifying if needed

    # q14 Have you had a dental exam in the past year?
    dentalExam = random.randint(1, 2)

    # q15 Have you had a flu shot this year?
    fluShot = random.randint(1, 2)

    # q16 Mental Health Questions
    # How satisfied are you with your work life?
    # 1 - Very Satisfied
    # 2 - Somewhat Satisfied
    # 3 - Somewhat Unsatisfied
    # 4 - Very Unsatisfied
    workLife = random.randint(1, 4)

    # How often do you feel stressed at work?
    # 1 - Never
    # 2 - Sometimes
    # 3 - Often
    # 4 - Continually
    workStress = random.randint(1, 4)

    # How many days did you miss from work (or school) due to illness or injury in the past 12 months?
    # 0-8 = # of days
    # 9 = 9+ days
    daysMissed = random.randint(0, 9)

    # During the past 4 weeks at work, how many days did poor physical or mental health result in lowered productivity?
    # 0-8 = # of days
    # 9 = 9+ days
    poorHealth = random.randint(0, 9)

    # By how much was your work output (productivity) generally impaired/decreased?
    # 0 - None
    # 1 - A little, 5%
    # 2 - Some, 15%
    # 3 - A lot 30%
    prodImpaired = random.randint(0, 3)

    # Rate your organizations interest in employee health and in creating a healthy work place.
    # 1 - Excellent
    # 2 - Good
    # 3 - Fair
    # 4 - Poor
    workplaceHealth = random.randint(1, 4)

    # EXERCISE----------------------------------------------------------------------------------------------------------
    # q17 How many days each week do you get at least 30 minutes of moderate to vigorous physical activity?
    #     (e.g., brisk walking, cycling, aerobics, hard physical labor)
    # 0-7 match how many days a week
    exerciseWeekly = random.randint(0, 7)

    # Do you have an exercise routine?
    exerciseRoutine = random.randint(1, 2)

    # q18 About how much time do you spend exercising each week?
    # 0-21 - hours per week FIXME not specified on excel sheet so took a guess at what encoding to use
    hoursExercising = random.randint(0, 21)

    # q19 Do you regularly do strength building exercise like weight lifting, push ups, crunches?
    strengthBuilding = random.randint(1, 2)
    # If yes, how many minutes per week do you engage in this exercise? TODO determine how this should be encoded

    # Do you regularly do stretching exercise like yoga or pilates?
    stretchingExercise = random.randint(1, 2)
    # If yes, how many minutes per week do you engage in this exercise?

    # EATING HABITS-----------------------------------------------------------------------------------------------------
    # q20 How often do you eat a healthy breakfast?
    # 1 - seldom
    # 2 - often/sometimes
    # 3 - daily or most days
    healthyBreakfast = random.randint(1, 3)

    # q21 portions
    # whole grain servings
    # 0-6 - 0-6+ servings
    wholeGrains = random.randint(0, 6)
    # cups of fruit
    # 0 - 0         5 - 2 1/2
    # 1 - 1/2       6 - 3
    # 2 - 1         7 - 3 1/2
    # 3 - 1 1/2     8 - 4
    # 4 - 2
    fruitServings = random.randint(0, 8)
    # cups of vegetables
    # encoding same as fruit above
    vegetableServings = random.randint(0, 8)
    # How many servings of protein do you eat daily?
    # 0 - 0         4 - 3
    # 1 - 1         5 - 3 1/2
    # 2 - 2         6 - 4+
    # 3 - 2 1/2
    proteinServings = random.randint(0, 6)
    # TODO add types of protein and fats eaten
    # How many servings of dairy do you eat daily?
    # 0-6 = 0-6+ servings
    dairyServings = random.randint(0, 6)
    # How many servings of nuts/seeds do you eat daily?
    # 0-6 = 0-6+ servings  # TODO find if serving encoding should change to fit daily vs. weekly
    nutServings = random.randint(0, 6)
    # How many sweets do you eat daily?
    # 0-6 = 0-6+
    sweetsServings = random.randint(0, 6)
    # How many cups of water do you drink daily?
    # 0-7 = 0-7+
    waterServings = random.randint(0, 7)
    # How much salt do you use in your diet?
    # 1 - use sparingly
    # 2 - don't limit
    # 3 - like salt
    saltServings = random.randint(1, 3)
    # q22 alcohol consumption in servings of alcohol
    alcohol = random.randint(1, 2)
    # 0 - none      3 - 8-14
    # 1 - 1-3       4 - 15-21
    # 2 - 4-7       5 - 22+
    alcoholServings = random.randint(0, 5)
    # How many times in the last 6 months did you drive within an hour of having 2 or more drinks, or ride with another
    # driver who had?
    # 0-8 = 0-8+ drinks
    alcoholDriving = random.randint(0, 8)

    # q23 smoking
    # Do you smoke?
    # 1 - never smoked
    # 2 - used to smoke (quit)
    # 3 - currently smoke
    smoke = random.randint(1, 3)
    if smoke == 3:
        packsPerDay = random.randint(0, 5)
        quitSmoking = -1
    elif smoke == 2:
        temp = random.randint(1, 12)
        yearOfBirth = random.randint(1920, 2002)
        # TODO check format of quit smoking date
        quitSmoking = str(random.randint(1, 12)) + '/' + str(random.randint(yearOfBirth + 12, 2019))
        packsPerDay = -1
    else:
        packsPerDay = -1
        quitSmoking = -1
    # secondhand smoke at work or home
    secondhandSmoke = random.randint(1, 2)

    # SOCIAL/HOME LIFE QUESTIONS----------------------------------------------------------------------------------------
    # q24 Are you married or living with a partner?
    married = random.randint(1, 2)
    # Do you make frequent contact with family and friends?
    frequentContact = random.randint(1, 2)
    # Do you regularly participate in a faith group?
    faithGroup = random.randint(1, 2)
    # Do you regularly participate in a social club?
    socialClub = random.randint(1, 2)
    # Are you careful to use safe sexual practices to prevent unintended pregnancies and sexually transmitted diseases
    # 1- always careful, 2 - sometimes careful, 3 - never careful
    safeSex = random.randint(1, 3)

    # q25 How often do you feel stressed at home?
    # 1 - Never
    # 2 - Sometimes
    # 3 - Often
    # 4 - Continually
    homeStress = random.randint(1, 4)
    # How often do you feel stressed about finances?
    # 1 - little or none
    # 2 - moderate
    # 3 - high or severe
    financialStress = random.randint(1, 3)
    # In the past year, have you been through any traumatic life events, like divorce, loss of a loved one, loss of job,
    # violence, major illness?
    # 0-3 = 0-3+
    traumaticEvents = random.randint(0, 3)
    # Do you ever use drugs (including prescriptions) that affect your mood or help you relax?
    # 1 - rarely or never, 2 - occasionally, 3 - almost every day
    moodDrugs = random.randint(1, 3)
    # TODO check how to encode how often mood altering drugs are taken
    # How many kinds of drugs did you take in the past month? This includes prescription and over the counter.
    # 0-8 = 0-8+
    drugsTaken = random.randint(0, 8)

    # SAFETY------------------------------------------------------------------------------------------------------------
    # q26 When driving or riding in a car, what percentage of the time do you wear a seatbelt?
    # 0 - 0%        3 - 70%
    # 1 - 25%       4 - 90%
    # 2 - 50%       5 -100%
    seatbelt = random.randint(0, 5)
    # Do children ever ride in your car?
    childrenCar = random.randint(1, 2)
    if childrenCar == 1:
        childSeat = random.randint(1, 2)
    else:
        childSeat = -1
    # How many miles per week do you usually drive or ride with others (average is 225 miles/week)?
    # 1 - high mileage, 2 - average mileage, 3 - low mileage
    mileageWeekly = random.randint(1, 3)
    # Does your home have a working smoke alarm near your sleeping areas?
    smokeAlarm = random.randint(1, 2)
    # When lifting heavy objects, do you use correct lifting technique?
    # 1 - always, 2 - sometimes or often, 3 - seldom or unsure
    liftingTechnique = random.randint(1, 3)
    # Are you careful to limit excess sun exposure and avoid sunburns?
    # same encoding as lifting
    sunSafety = random.randint(1, 3)
    # Do you ever ride motorcycles or bicycles, ski or snowboard?
    bikesAndSkis = random.randint(1, 2)
    # Wear helmets if yes
    if bikesAndSkis == 1:
        wearHelmet = random.randint(1, 2)
    else:
        wearHelmet = -1
    qTuple = {
        "Name": Name,
        "Gender": gender,
        "Date of Birth": DOB,
        "Height": height,
        "Weight": weight,
        "Race/Ethnicity": race,
        "Health Status": health,
        "Hours of Sleep": hrSleep,
        "Physical in the last 2 years?": physical2years,
        "Allergies": allergies,
        "Asthma": asthma,
        "Arthritis": arthritis,
        "Chronic Back Pain": backPain,
        "COPD": COPD,
        "Chronic Sinus Problems": sinusProblems,
        "Heart Disease or Angina": angina,
        "Broken Bones or Fractures": brokenBones,
        "Heart Surgery": heartSurgery,
        "Blood Pressure Check": bpCheck,
        "Normal or Elevated Blood Pressure": normalBP,
        "Blood Pressure Medication": bpMeds,
        "Cholesterol Check": cholesterolCheck,
        "Normal or Elevated Cholesterol": normalCholesterol,
        "Cholesterol Medication": cholesterolMeds,
        "History of Cancer": cancerHistory,
        "Age of Diagnosis": cancerAge,
        "Pap Test in Past 3 Years": papTest,
        "Normal or Abnormal Pap Test": papTestNormal,
        "Mammogram in 2 Years": mammogram,
        "Normal or Abnormal Mammogram": mammogramNormal,
        "Diabetes": diabetes,
        "Blood Sugar Check": bloodSugarCheck,
        "Normal Blood Sugar": normalBloodSugar,
        "Diabetes Medication": diabetesMeds,
        "Stroke": stroke,
        "Other Medication": otherMeds,
        "Over the Counter Medication": overCounterMeds,
        "Take Supplements": supplements,
        "Dental Exam": dentalExam,
        "Flu Shot": fluShot,
        "Work Life Satisfaction": workLife,
        "Work Stress": workStress,
        "Days Missed from Illness or Injury": daysMissed,
        "Days Missed from Poor Mental or Physical Health": poorHealth,
        "Affect on Productivity": prodImpaired,
        "Organization Interest in Health": workplaceHealth,
        "Days of Exercise a Week": exerciseWeekly,
        "Exercise Routine": exerciseRoutine,
        "Hours of Exercise a Week": hoursExercising,
        "Strength Building": strengthBuilding,
        "Stretching Exercise": stretchingExercise,
        "Healthy Breakfast": healthyBreakfast,
        "Whole Grain Servings": wholeGrains,
        "Fruit Servings": fruitServings,
        "Vegetable Servings": vegetableServings,
        "Protein Servings": proteinServings,
        "Dairy Servings": dairyServings,
        "Nut Servings": nutServings,
        "Sweets Servings": sweetsServings,
        "Cups of Water": waterServings,
        "Salt Servings": saltServings,
        "Drink Alcohol": alcohol,
        "Alcoholic Drinks Per Week": alcoholServings,
        "Driving/Riding After 2 Drinks": alcoholDriving,
        "Smoking Status": smoke,
        "Date Quit Smoking": quitSmoking,
        "Packs Per Day": packsPerDay,
        "Secondhand Smoke": secondhandSmoke,
        "Married or Living with Partner": married,
        "Frequent Contact with Friends or Family": frequentContact,
        "Faith Group": faithGroup,
        "Social Club": socialClub,
        "Safe Sexual Practices": safeSex,
        "Stress at Home": homeStress,
        "Financial Stress": financialStress,
        "Traumatic Events": traumaticEvents,
        "Use of Mood Altering Drugs": moodDrugs,
        "Number of Kinds of Drugs Taken": drugsTaken,
        "Seatbelt Worn": seatbelt,
        "Children in Car": childrenCar,
        "Children Use Child Seat": childSeat,
        "Weekly Driving Mileage": mileageWeekly,
        "Smoke Alarm Near Sleeping Areas": smokeAlarm,
        "Use of Correct Lifting Technique": liftingTechnique,
        "Use of Sunscreen and Sun Protection": sunSafety,
        "Riding Bikes, Motorcycles, Skis, or Snowboards": bikesAndSkis,
        "Wear Helmets": wearHelmet
    }

    # load existing json file
    with open(fName) as feed_json:
        feeds = json.load(feed_json)

    # append new data and save json
    feeds.append(qTuple)
    with open(fName, mode='w') as f:
        f.write(json.dumps(feeds, indent=2))

    # # q2 Race/Ethnicity
    # q2 = random.randint(1, 6)
    #
    # # q3 Personal Health History
    # q3a = random.randint(1, 2)
    # q3b = random.randint(1, 2)
    # q3c = random.randint(1, 2)
    # q3d = random.randint(1, 2)
    # q3e = random.randint(1, 2)
    # q3f = random.randint(1, 2)
    # q3g = random.randint(1, 2)
    # q3h = random.randint(1, 2)
    # q3i = random.randint(1, 2)
    # q3j = random.randint(1, 2)
    # q3k = random.randint(1, 2)
    #
    # # q4 Overall Health
    # q4 = random.randint(1, 5)
    #
    # # q5 preventative health tests
    # q5a = random.randint(1, 2)
    # q5b = random.randint(1, 2)
    # q5c = random.randint(1, 2)
    # q5d = random.randint(1, 2)
    # q5e = random.randint(1, 2)
    # q5f = random.randint(1, 2)
    # q5g = random.randint(1, 2)
    # q5h = random.randint(1, 2)
    # q5i = random.randint(1, 2)
    # q5j = random.randint(1, 2)
    #
    # # q6 Common health tests
    # q6a = random.randint(1, 4)
    # q6b = random.randint(1, 4)
    # q6c = random.randint(1, 4)
    #
    # # q7 Medications
    # q7a = random.randint(1, 2)
    # q7b = random.randint(1, 2)
    # q7c = random.randint(1, 2)
    #
    # # q8 Sick Days
    # q8 = random.randint(0, 9)
    #
    # # q9 Exercise days
    # q9 = random.randint(0, 7)
    #
    # # q10 Strength Exercise
    # q10 = random.randint(0, 3)
    #
    # # q11 stretching exercise
    # q11 = random.randint(0, 3)
    #
    # # q12 breakfast
    # q12 = random.randint(1, 3)
    #
    # # q13 whole grains
    # q13 = random.randint(0, 6)
    #
    # # q14 Fruits
    # q14 = random.randint(0, 8)
    #
    # # q15 Vegetables
    # q15 = random.randint(0, 8)
    #
    # # q16 Protein
    # q16 = random.randint(0, 6)
    #
    # # q17 Kind of proteins
    # q17 = random.randint(1, 3)
    #
    # # q18 Fats
    # q18 = random.randint(1, 3)
    #
    # # q19 dairy
    # q19 = random.randint(0, 6)
    #
    # # q20 Nuts/Seeds
    # q20 = random.randint(0, 6)
    #
    # # q21 sweets
    # q21 = random.randint(0, 5)
    #
    # # q22 water
    # q22 = random.randint(0, 7)
    #
    # # q23 salt
    # q23 = random.randint(1, 3)
    #
    # # q24 supplements
    # q24a = random.randint(1, 2)  # Calcium
    # q24b = random.randint(1, 2)  # Vitamin D
    # q24c = random.randint(1, 2)  # Vitamin B12
    # q24d = random.randint(1, 2)  # multivitamin/mineral
    #
    # # q25 smoking status
    # q25 = random.randint(1, 3)
    #
    # # q26 secondhand smoke
    # q26 = random.randint(1, 2)
    #
    # # q27 alcohol
    # q27 = random.randint(0, 5)
    #
    # # q28 drugs
    # q28 = random.randint(1, 3)
    #
    # # q29 kinds of drugs
    # q29 = random.randint(0, 8)
    #
    # # q30 stress at work
    # q30 = random.randint(1, 4)
    #
    # # q31 stress at home
    # q31 = random.randint(1, 4)
    #
    # # q32 stress from finance
    # q32 = random.randint(1, 3)
    #
    # # q33 traumatic life experiences
    # q33 = random.randint(0, 3)
    #
    # # q34 Outlook
    # q34 = random.randint(1, 3)
    #
    # # q35 control
    # q35 = random.randint(1, 4)
    #
    # # q36 Happiness
    # q36 = random.randint(1, 3)
    #
    # # q37 Mood
    # q37 = random.randint(1, 2)
    #
    # # q38 Functioning
    # q38 = random.randint(1, 2)
    #
    # # q39 Relax
    # q39 = random.randint(1, 3)
    #
    # # q40 energy
    # q40 = random.randint(1, 3)
    #
    # # q41 satisfaction
    # q41 = random.randint(1, 4)
    #
    # # q42 social support
    # q42a = random.randint(1, 2)  # married/significant other
    # q42b = random.randint(1, 2)  # frequent contact with family and friends
    # q42c = random.randint(1, 2)  # participate in faith group
    # q42d = random.randint(1, 2)  # participate in social group
    #
    # # q43 sleep
    # q43 = random.randint(1, 4)
    #
    # # q44 seat belts
    # q44 = random.randint(0, 5)
    #
    # # q45 child safety seats
    # q45 = random.randint(1, 3)
    #
    # # q46 drinking and driving
    # q46 = random.randint(0, 8)
    #
    # # q47 smoke alarm
    # q47 = random.randint(1, 2)
    #
    # # q48 driving
    # q48 = random.randint(1, 3)
    #
    # # q49 Lifting
    # q49 = random.randint(1, 3)
    #
    # # q50 Sun
    # q50 = random.randint(1, 3)
    #
    # # q51 Helmets
    # q51 = random.randint(1, 3)
    #
    # # q52 Optional Question, STD
    # q52 = random.randint(1, 3)
    #
    # # q53 Work Life
    # q53 = random.randint(1, 4)
    #
    # # q54 Productivity
    # q54 = random.randint(0, 9)
    #
    # # q55 Limitations
    # q55 = random.randint(0, 3)
    #
    # # q56 Health Culture
    # q56 = random.randint(1, 4)
    #
    # # q57 lifestyle changes
    # q57a = random.randint(1, 5)  # physically active
    # q57b = random.randint(1, 5)  # practice good eating habits
    # q57c = random.randint(1, 5)  # avoid smoking or using tobacco
    # q57d = random.randint(1, 5)  # lose weight or maintain a healthy weight
    # q57e = random.randint(1, 5)  # cope better with stress
    # q57f = random.randint(1, 5)  # lower or maintain healthy cholesterol level
    # q57g = random.randint(1, 5)  # lower or maintain healthy blood pressure
    # q57h = random.randint(1, 5)  # avoid alcohol or drink in moderation
    # q57i = random.randint(1, 5)  # live an overall healthy lifestyle

    # # create tuple for output
    # qTuple = {"q1a": q1a,
    #           "q1b": q1b,
    #           "q2":  q2,
    #           "q3a": q3a,
    #           "q3b": q3b,
    #           "q3c": q3c,
    #           "q3d": q3d,
    #           "q3e": q3e,
    #           "q3f": q3f,
    #           "q3g": q3g,
    #           "q3h": q3h,
    #           "q3i": q3i,
    #           "q3j": q3j,
    #           "q3k": q3k,
    #           "q4": q4,
    #           "q5a": q5a,
    #           "q5b": q5b,
    #           "q5c": q5c,
    #           "q5d": q5d,
    #           "q5e": q5e,
    #           "q5f": q5f,
    #           "q5g": q5g,
    #           "q5h": q5h,
    #           "q5i": q5i,
    #           "q5j": q5j,
    #           "q6a": q6a,
    #           "q6b": q6b,
    #           "q6c": q6c,
    #           "q7a": q7a,
    #           "q7b": q7b,
    #           "q7c": q7c,
    #           "q8": q8,
    #           "q9": q9,
    #           "q10": q10,
    #           "q11": q11,
    #           "q12": q12,
    #           "q13": q13,
    #           "q14": q14,
    #           "q15": q15,
    #           "q16": q16,
    #           "q17": q17,
    #           "q18": q18,
    #           "q19": q19,
    #           "q20": q20,
    #           "q21": q21,
    #           "q22": q22,
    #           "q23": q23,
    #           "q24a": q24a,
    #           "q24b": q24b,
    #           "q24c": q24c,
    #           "q24d": q24d,
    #           "q25": q25,
    #           "q26": q26,
    #           "q27": q27,
    #           "q28": q28,
    #           "q29": q29,
    #           "q30": q30,
    #           "q31": q31,
    #           "q32": q32,
    #           "q33": q33,
    #           "q34": q34,
    #           "q35": q35,
    #           "q36": q36,
    #           "q37": q37,
    #           "q38": q38,
    #           "q39": q39,
    #           "q40": q40,
    #           "q41": q41,
    #           "q42a": q42a,
    #           "q42b": q42b,
    #           "q42c": q42c,
    #           "q42d": q42d,
    #           "q43": q43,
    #           "q44": q44,
    #           "q45": q45,
    #           "q46": q46,
    #           "q47": q47,
    #           "q48": q48,
    #           "q49": q49,
    #           "q50": q50,
    #           "q51": q51,
    #           "q52": q52,
    #           "q53": q53,
    #           "q54": q54,
    #           "q55": q55,
    #           "q56": q56,
    #           "q57a": q57a,
    #           "q57b": q57b,
    #           "q57c": q57c,
    #           "q57d": q57d,
    #           "q57e": q57e,
    #           "q57f": q57f,
    #           "q57g": q57g,
    #           "q57h": q57h,
    #           "q57i": q57i
    #           }

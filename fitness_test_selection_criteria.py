''' Problem Statement
Write a Python function avg_oxygen(oxygen_levels) that evaluates the oxygen levels of trainees participating in a fitness test and determines the most fit trainee(s) based on their average oxygen levels
over three rounds. The function should return a list of tuples containing the trainee number and their respective average oxygen level. If multiple trainees have the same highest average oxygen level, 
include all of them in the list. If the average oxygen level of all trainees is below 70, declare all trainees as unfit.

OUTPUT :-
Enter the oxygen level of trainee 1 - Round 1: 95
Enter the oxygen level of trainee 2 - Round 1: 90
Enter the oxygen level of trainee 3 - Round 1: 95
Enter the oxygen level of trainee 1 - Round 2: 92
Enter the oxygen level of trainee 2 - Round 2: 90
Enter the oxygen level of trainee 3 - Round 2: 92
Enter the oxygen level of trainee 1 - Round 3: 90
Enter the oxygen level of trainee 2 - Round 3: 95
Enter the oxygen level of trainee 3 - Round 3: 90
Trainee Number 1
Trainee Number 3

'''

def avg_oxygen(oxygen_levels):
    if len(oxygen_levels) < 9:
        return []

    t1 = (oxygen_levels[0] + oxygen_levels[3] + oxygen_levels[6]) / 3
    t2 = (oxygen_levels[1] + oxygen_levels[4] + oxygen_levels[7]) / 3
    t3 = (oxygen_levels[2] + oxygen_levels[5] + oxygen_levels[8]) / 3
    
    average = (t1 + t2 + t3) / 3
    
    if average > 70:
        max_average = max(t1, t2, t3)
        max_trainees = []
        if t1 == max_average:
            max_trainees.append(("Trainee Number 1", t1))
        if t2 == max_average:
            max_trainees.append(("Trainee Number 2", t2))
        if t3 == max_average:
            max_trainees.append(("Trainee Number 3", t3))
        return max_trainees
    else:
        return []

oxygen_levels = []
for t in range(1, 4): 
    for r in range(1, 4): 
        while True:
            n = int(input(f"Enter the oxygen level of trainee {r} - Round {t}: "))
            if 0 < n <= 100:
                oxygen_levels.append(n)
                break  
            else:
                print("Invalid input. Oxygen level must be between 1 and 100.")

results = avg_oxygen(oxygen_levels)
if results:
    for trainee, oxygen in results:
        print(trainee)
else:
    print("All are unfit")

import random

# List of male and female students
male_students = ["Male1", "Male2", "Male3", "Male4", "Male5", "Male6", "Male7", "Male8", "Male9", "Male10",
                 "Male11", "Male12", "Male13", "Male14", "Male15", "Male16", "Male17", "Male18", "Male19", "Male20"]
female_students = ["Female1", "Female2", "Female3", "Female4", "Female5", "Female6", "Female7", "Female8", 
                   "Female9", "Female10", "Female11", "Female12", "Female13", "Female14", "Female15", "Female16", 
                   "Female17", "Female18", "Female19", "Female20", "Female21", "Female22", "Female23", "Female24", 
                   "Female25", "Female26", "Female27", "Female28", "Female29", "Female30", "Female31", "Female32", 
                   "Female33", "Female34", "Female35", "Female36"]

# Shuffle the male and female lists
random.shuffle(male_students)
random.shuffle(female_students)

# Function to generate teams
def create_teams(male_students, female_students):
    teams = []
    
    # Create male-only teams
    for i in range(0, len(male_students) - len(male_students) % 3, 3):
        teams.append([male_students[i], male_students[i+1], male_students[i+2]])
    
    # Create female-only teams
    for i in range(0, len(female_students) - len(female_students) % 3, 3):
        teams.append([female_students[i], female_students[i+1], female_students[i+2]])
    
    # If there are any remaining students, create mixed teams
    remaining_males = male_students[len(male_students) - len(male_students) % 3:]
    remaining_females = female_students[len(female_students) - len(female_students) % 3:]
    
    mixed_students = remaining_males + remaining_females
    random.shuffle(mixed_students)
    
    for i in range(0, len(mixed_students) - len(mixed_students) % 3, 3):
        teams.append([mixed_students[i], mixed_students[i+1], mixed_students[i+2]])
    
    return teams

# Generate teams
teams = create_teams(male_students, female_students)

# Display the teams
for idx, team in enumerate(teams):
    print(f"Team {idx+1}: {team}")
################################
# Pema Dolker
# SWE
# 02230294
################################
# REFERENCES
# Links that you referred while solving: phind and chatgpt
# the problem: no problem faced
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score:
# Task 1: There were 20000 people assigned and there are 6424 of overlapping space assignments
# Task 2: There were 2457 assignments that overlap completely.
#https://github.com/pemadolker?tab=repositories
################################

# Read the input.txt file
def read_input():
    # Open the input file and read its lines
    with open(r"C:\Users\DELL\Downloads\input_4_cap2.txt", 'r') as file:
        lines = file.readlines()
    assignments = []
    # Parse the input lines into a list of assignments
    for line in lines:
        line = line.strip().split(", ")
        assignments.append([tuple(map(int, space.split("-"))) for space in line])
    return assignments

# Solution for Task 1
def task_1(assignments):
    # Function to check if two ranges overlap
    def ranges_overlap(r1, r2):
        return max(r1[0], r2[0]) <= min(r1[1], r2[1])

    # Calculate the total number of people assigned
    total_people = sum(len(line) for line in assignments)
    overlapping_count = 0
    # Count the number of overlapping space assignments
    for line in assignments:
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if ranges_overlap(line[i], line[j]):
                    overlapping_count += 1
    print(f" There were {total_people} people assigned and there are {overlapping_count} of overlapping space assignments.")

# Solution for Task 2
def task_2(assignments):
    complete_overlap_count = 0
    # Count the number of assignments that overlap completely
    for line in assignments:
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i][0] <= line[j][0] and line[i][1] >= line[j][1]:
                    complete_overlap_count += 1
    print(f" There were {complete_overlap_count} assignments that overlap completely.")

# Other parts of code here to run your functions and printing of the required solution.
assignments = read_input()
task_1(assignments)
task_2(assignments)



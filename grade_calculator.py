grade_file = input("Enter the name of the grade file: ")
# grade_file = "test_files/grades1.test.dat"

lab_name = []
lab_grade = []
hw_name = []
hw_grade = [] 
project_name = []
project_grade = []
exam_name = []
exam_grade = []
final_exam_name = []
final_exam_grade = []

def file_parse(iterator, assignments_1:str, name_list:list, grade_list:list, assignments_2:str=None):
    """
    Function to sort the data into the specified category.
    """
    if iterator.startswith(assignments_1) or (assignments_2 and iterator.startswith(assignments_2)):
        assignment, grade = iterator.strip().split(", ")
        name_list.append(assignment)
        grade_list.append(grade)

def safe_division(num:int, den:int):
    try:
        return num/den
    except ZeroDivisionError:
        return 0
    
def grade_sum_weighted(grade_list:list, points:int, weight:float, drop:bool = False, number_drop:int=0):
    """
    Function to calculate the grades of all categories outside of grades.
    Returns a list of weighted and raw grades for each category
    """
    if drop == True:
        grade_list = grade_list.copy()
        grade_list.sort()
        grade_list = grade_list[number_drop:]

    grade_total = 0
    Assignment_count = 0

    for i in grade_list:
        grade_total += int(i)
        Assignment_count += 1
    # weighted_grade = (safe_division(grade_total, (Assignment_count*points))*100)*weight
    raw_grade = round(safe_division(grade_total, (Assignment_count*points))*100,1)

    return grade_total, Assignment_count*points, raw_grade

def exam_grade_calc(grade_list:list, points:int, weight:float):
    """
    Function to calculate the grades of midterms. 
    Returns a list of weighted and raw grades for each midterm. 
    """
    # weighted_grades = [round((((float(i)/points) * 100)*weight),6) for i in grade_list]
    raw_grade = [round(safe_division(int(i), points) * 100,1) for i in grade_list]
    return raw_grade
        
def calculate_full_weight():
    contribution_lab = contribution_final = contribution_exam = contribution_project = contribution_hw = 0
    if score_present(lab_name):
        contribution_lab = 0.100
    if score_present(hw_name):
        contribution_hw = .150
    if score_present(project_name):
        contribution_project = .250
    if score_present(exam_name):
        contribution_exam = .150 * len(exam_name)
    if score_present(final_exam_name):
        contribution_final = .200
    return (contribution_project + contribution_exam + contribution_final + contribution_hw + contribution_lab)


def calculate_final_grade(lab_raw:float, hw_raw:float, project_raw:float, exam_raw:list, final_raw:float, full_raw:float):
    """
    Function to determine the final grade based off of the calculated individual weighted grades
    """
    final_grade = (lab_raw * 0.1) + (hw_raw * .15) + (project_raw * .25) + (final_raw * .20)
    for grade in exam_raw:
        final_grade += (grade * .15)
    return (final_grade/full_weight)

def score_present(score_list:list):
    """
    Function to determine if there are scores present for each category. 
    """
    if score_list == []:
        return False
    else:
        return True

def calculate_letter(final_grade:float):
    """
    Function to determine the final letter grade from the calculated final grade percent.
    """
    if final_grade >= 93:
        return "A"
    elif 93 > final_grade >= 90:
        return "A-"
    elif 90 > final_grade >= 87:
        return "B+"
    elif 87 > final_grade >= 83:
        return "B"
    elif 83 > final_grade >= 80:
        return "B-"
    elif 80 > final_grade >= 77:
        return "C+"
    elif 77 > final_grade >= 73:
        return "C"
    elif 73 > final_grade >= 70:
        return "C-"
    elif 70 > final_grade >= 67:
        return "D+"
    elif 67 > final_grade >= 63:
        return "D"
    elif 63 > final_grade >= 60:
        return "D-"
    elif 60 > final_grade:
        return "E"

# Reading in Data
with open(grade_file, 'r') as file:
    for line in file:
        file_parse(line, "Lab", lab_name, lab_grade)
        file_parse(line, "Homework", hw_name, hw_grade)
        file_parse(line, "Project", project_name, project_grade, "FreeCoding")
        file_parse(line, "Midterm", exam_name, exam_grade)
        file_parse(line, "Final", final_exam_name, final_exam_grade)

# Calculating Grades
lab_points_earned, lab_points_possible, lab_raw = grade_sum_weighted(lab_grade, 20, .10, True, 2)
hw_points_earned, hw_points_possible, hw_raw = grade_sum_weighted(hw_grade, 50, .15, True, 1)
project_points_earned, project_points_possible, project_raw = grade_sum_weighted(project_grade, 100, .25)
exam_raw = exam_grade_calc(exam_grade, 40, .15)
final_points_earned, final_points_possible, final_raw = grade_sum_weighted(final_exam_grade, 70, .20)

# Checking if all scores are available and returning the weight of the available scores
full_weight = calculate_full_weight()

# Calculating final grades
final_class_grade = calculate_final_grade(lab_raw, hw_raw, project_raw, exam_raw, final_raw, full_weight)
letter_grade = calculate_letter(final_class_grade)

# Returning Results
# print("Category\tPoints\tPercentage")
if score_present(lab_name):
    print(f"Labs:\t{lab_points_earned}/{lab_points_possible}\t{lab_raw:.1f}%")

if score_present(hw_name):
    print(f"Homework:\t{hw_points_earned}/{hw_points_possible}\t{hw_raw:.1f}%")

if score_present(project_name):
    print(f"Projects:\t{project_points_earned}/{project_points_possible}\t{project_raw:.1f}%")

if score_present(exam_name):
    for i, name in enumerate(exam_name):
        print(f"{name}:\t{exam_grade[i]}/40\t{exam_raw[i]:.1f}%")

if score_present(final_exam_name):
    print(f"Final:\t{final_points_earned}/{final_points_possible}\t{final_raw:.1f}%")
    
print(f"The overall grade in the class is: {letter_grade} ({final_class_grade:.2f}%)")



# corrections to be made: make the points separate values of type int.



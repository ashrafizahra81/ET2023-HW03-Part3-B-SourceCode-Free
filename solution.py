import json
import operator

file_name = input("enter the name of the file: ")

file_path = 'D:/Uni/Sem8/ET2/ET2023-HW03-Part3-B-CODE-Rd-Free/ET2023-HW03-Part3-B-SourceCode-Free/' + file_name
with open(file_path, 'r') as file:
    json_data = json.load(file)


utils = json_data['utilities']
max_util = max(utils.items(), key=operator.itemgetter(1))[0]
max_util_value = utils[max_util]
actions = json_data['actions']
consequences = json_data['consequences']
mechanisms = json_data['mechanisms']

conseq = max_util
cause = str

while True:

    cause = mechanisms[conseq]
    if cause in actions or "Not" in cause:
        break
    conseq = cause

problem_description = "This is the solution of the "+ file_name.split(".")[0] + " problem in relativism"
goal = max_util
initialState = {}
for c in consequences:
    initialState[c] = "False"
intentions = {}
intentions[max_util] = cause
solution = "In relativism and based on its principles the maximum utility is for " + cause + ", with " + str(max_util_value) + ', which causes to "' + max_util + '" consequence.'

output_dict = {}
output_dict["problem_description"] = problem_description
output_dict["initialState"] = initialState
output_dict["solution"] = solution
output_dict["goal"] = goal
output_dict["intentions"] = intentions


output_file_path = 'D:/Uni/Sem8/ET2/ET2023-HW03-Part3-B-CODE-Rd-Free/ET2023-HW03-Part3-B-SourceCode-Free/output/' + "output_" + file_name 
with open(output_file_path, 'w') as file:
    
    json.dump(output_dict, file, indent=4)

print("JSON file created successfully.")

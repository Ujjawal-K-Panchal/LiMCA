import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def execute_function_definition(definition):
    exec(definition, globals())

def compare_results(result, expected_result):
    return str(result) == str(expected_result).strip()

if __name__ == "__main__":
    function_definition_folder = "refactory_q1/q1_GPT_sol_iter_1"
    function_defs = []
    for filename in os.listdir(function_definition_folder):
        file_path = os.path.join(function_definition_folder, filename)
        if os.path.isfile(file_path):
            function_defs.append(read_file(file_path))


    # Get function calls from a folder
    function_call_folder = "refactory_q1/q1_inputs"
    function_calls = []
    for filename in os.listdir(function_call_folder):
        file_path = os.path.join(function_call_folder, filename)
        if os.path.isfile(file_path):
            function_calls.append(read_file(file_path))

    # Get expected results from another folder
    expected_results_folder = "refactory_q1/q1_outputs"
    expected_results = []
    for filename in os.listdir(expected_results_folder):
        file_path = os.path.join(expected_results_folder, filename)
        if os.path.isfile(file_path):
            expected_results.append(read_file(file_path))

    # Ensure the number of function calls matches the number of expected results
    if len(function_calls) != len(expected_results):
        print("Error: Number of function calls does not match the number of expected results.")
        exit()

    filenum=0
    for function_def in function_defs:
        filenum+=1
        # Counter for the number of expected results
        num_expected_results = 0

        # Execute the function definition
        execute_function_definition(function_def)

        # Iterate through pairs of function calls and expected results
        for function_call, expected_result in zip(function_calls, expected_results):
            # Execute the function call and capture the result
            result = eval(function_call)
            # Compare the result with the expected result
            if compare_results(str(result), expected_result):
                num_expected_results += 1

        print("Number of expected results: for file ", filenum, ": ", num_expected_results,"/",len(expected_results))

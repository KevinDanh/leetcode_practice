import unittest
import xml.etree.ElementTree as ET
import os
import sys

def load_problem_map():
    """Parses XML and returns a sorted dictionary mapping problem IDs to test paths."""
    tree = ET.parse("problem_map.xml")
    root = tree.getroot()
    problem_list = []

    for problem in root.findall("problem"):
        problem_id = int(problem.attrib["id"])  # Convert ID to integer for correct sorting
        problem_name = problem.find("name").text
        display_name = f"{problem_id} - {problem_name}"  # Format: "ID - Name"
        test_path = problem.find("test_path").text
        problem_list.append((problem_id, display_name, test_path))

    # Sort problems strictly by numerical ID
    problem_list.sort()

    return {str(item[0]): item[2] for item in problem_list}  # Mapping "ID" (as string) to test_path

def run_test(problem_number, problem_map):
    """Runs the test for the specified problem number."""
    if problem_number in problem_map:
        test_file = os.path.basename(problem_map[problem_number])  # Extract test filename
        test_dir = os.path.dirname(problem_map[problem_number])  # Extract test directory
        
        loader = unittest.TestLoader()
        tests = loader.discover(test_dir, pattern=test_file)
        runner = unittest.TextTestRunner()
        runner.run(tests)
    else:
        print(f"Error: Problem {problem_number} not found.")

if __name__ == "__main__":
    problem_map = load_problem_map()

    # Check if a problem number was passed as an argument
    if len(sys.argv) > 1:
        problem_number = sys.argv[1].strip()  # Get problem number from command-line args
        run_test(problem_number, problem_map)
    else:
        print("Available problems:")
        for problem_id, test_path in problem_map.items():
            print(f"{problem_id}: {test_path}")

        problem_number = input("Enter problem number to test: ").strip()
        run_test(problem_number, problem_map)

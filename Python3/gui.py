import os
import io
import sys
import unittest
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QTextEdit

class TestRunnerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LeetCode Test Runner")
        self.setGeometry(2000, 500, 400, 200)  # Adjust window placement if needed

        layout = QVBoxLayout()

        self.problem_map = self.load_problem_map()

        # Ensure sorting by problem ID
        sorted_problems = sorted(self.problem_map.keys(), key=lambda x: int(x.split(" - ")[0]))
        self.test_selector = QComboBox()
        self.test_selector.addItems(sorted_problems)  # Sorted list of "ID - Name"
        layout.addWidget(self.test_selector)

        self.run_button = QPushButton("Run Test")
        self.run_button.clicked.connect(self.run_selected_test)
        layout.addWidget(self.run_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def load_problem_map(self):
        """Parses XML and returns a sorted dictionary mapping problem names to test paths."""
        tree = ET.parse("problem_map.xml")
        root = tree.getroot()
        problem_list = []

        for problem in root.findall("problem"):
            problem_id = int(problem.attrib["id"])
            problem_name = problem.find("name").text
            display_name = f"{problem_id} - {problem_name}"  # Format: "ID - Name"
            test_path = problem.find("test_path").text
            problem_list.append((problem_id, display_name, test_path))

        # Sort problems strictly by numerical ID
        problem_list.sort()

        return {item[1]: item[2] for item in problem_list}  # Mapping "ID - Name" to test_path

    def run_selected_test(self):
        """Runs the selected test using unittest."""
        selected_problem = self.test_selector.currentText()
        test_path = self.problem_map.get(selected_problem, None)

        if test_path:
            test_file = os.path.basename(test_path)  # Extract file name
            test_dir = os.path.dirname(test_path)  # Extract directory

            # Redirect stdout to capture unittest output
            output_buffer = io.StringIO()
            sys.stdout = output_buffer  # Redirect console output
            sys.stderr = output_buffer  # Redirect console output

            loader = unittest.TestLoader()
            tests = loader.discover(test_dir, pattern=test_file)
            runner = unittest.TextTestRunner()
            result = runner.run(tests)

            # Reset stdout and capture output
            sys.stdout = sys.__stdout__  # Restore original stdout
            sys.stderr = sys.__stderr__  # Restore original stdout
            captured_output = output_buffer.getvalue()  # Get captured test results

            self.output.setText(str(captured_output))

if __name__ == "__main__":
    app = QApplication([])
    window = TestRunnerGUI()
    window.show()
    app.exec()

import unittest
import os

# Load all test cases from the 'tests' directory
loader = unittest.TestLoader()

# Use the current directory and the tests folder path
suite = loader.discover(os.path.join(os.path.dirname(__file__), 'tests'))

# Run the tests
runner = unittest.TextTestRunner()
runner.run(suite)

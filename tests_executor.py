import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Please provide test to execute as comma-separated list: e.g. 1,2,3")
    test_numbers = [int(x.strip()) for x in sys.argv[1].split(",")]
    print("=" * 100)
    for test_number in test_numbers:
        os.system(f"python tests.py {test_number}")
    print("=" * 100)

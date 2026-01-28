from functions.get_file_content import get_file_content
from config import MAX_CHARS

def run_tests():
    # Test lorem.txt (truncate)
    print("Test: lorem.txt truncation")
    content = get_file_content("calculator", "lorem.txt")
    print(f"  Length: {len(content)}")
    print(f"  Truncated message present: {'truncated' in content}")

    # Files expected to be small — print full content
    for file_path in ["main.py", "pkg/calculator.py"]:
        print(f"\nTest: {file_path}")
        result = get_file_content("calculator", file_path)
        print(result)  # no truncation

    # Outside working directory
    print("\nTest: /bin/cat")
    result = get_file_content("calculator", "/bin/cat")
    print(result)

    # Nonexistent file
    print("\nTest: pkg/does_not_exist.py")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    run_tests()

from functions.write_file import write_file

def run_tests():
    tests = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]

    for working_dir, file_path, content in tests:
        print(f'Test: write_file("{working_dir}", "{file_path}")')
        result = write_file(working_dir, file_path, content)
        print(f'  {result}\n')

if __name__ == "__main__":
    run_tests()


from functions.get_files_info import get_files_info

def run_tests():
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    if result.startswith("Error:"):
        print(f"  {result}")
    else:
        for line in result.splitlines():
            print(f"  {line}")

    print("\nResult for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    if result.startswith("Error:"):
        print(f"  {result}")
    else:
        for line in result.splitlines():
            print(f"  {line}")

    print("\nResult for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print(f"  {result}")

    print("\nResult for '../' directory:")
    result = get_files_info("calculator", "../")
    print(f"  {result}")

if __name__ == "__main__":
    run_tests()
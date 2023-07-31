def count_strings_with_same_first_and_last(strings_list):
    count = 0
    for string in strings_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

def main():
    # Example list of strings
    strings_list = ["abc", "dda", "deed", "hello", "wow", "xyz", "abca", "bcb", "z"]
    
    count = count_strings_with_same_first_and_last(strings_list)
    print("Number of strings where the first and last character are the same:", count)

#if __name__ == "__main__":
#     main()

main()
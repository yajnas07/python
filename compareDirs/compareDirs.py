import os
import filecmp

# def compare_directories(dir1, dir2):
#     # Compare the contents of the two directories
#     comparison = filecmp.dircmp(dir1, dir2)

#     # Print the names of the files and directories that are only in dir1
#     for name in comparison.left_only:
#         print(f"Only in {dir1}: {name}")

#     # Print the names of the files and directories that are only in dir2
#     for name in comparison.right_only:
#         print(f"Only in {dir2}: {name}")

#     # Print the names of the files and directories that are in both directories but have different contents
#     for name in comparison.diff_files:
#         print(f"Different in {dir1} and {dir2}: {name}")

#     # Recursively compare the contents of the subdirectories
#     if hasattr(comparison, 'subdirs'):
#       for subdir in comparison.subdirs.values():
#         compare_directories(os.path.join(dir1, subdir.name), os.path.join(dir2, subdir.name))



def compare_directories(dir1, dir2):
    # Compare the contents of the two directories
    comparison = filecmp.dircmp(dir1, dir2)

    # Print the names of the files and directories that are only in dir1
    for name in comparison.left_only:
        print(f"Only in {dir1}: {name}")

    # Print the names of the files and directories that are only in dir2
    for name in comparison.right_only:
        print(f"Only in {dir2}: {name}")

    # Print the names of the files and directories that are in both directories but have different contents
    for name in comparison.diff_files:
        file1 = os.path.join(dir1, name)
        file2 = os.path.join(dir2, name)
        if filecmp.cmp(file1, file2):
            print(f"Different in {dir1} and {dir2}: {name}")

    # Recursively compare the contents of the subdirectories
    for subdir in comparison.subdirs.values():
        print(subdir);
        compare_directories(os.path.join(dir1, subdir), os.path.join(dir2, subdir))



a  = os.curdir
print(str(a));
compare_directories("./test1", "./test2");
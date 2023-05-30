import sys

from controllers import find_duplicate_files


def run_serverless(directory_to_scan):
    
    duplicates = find_duplicate_files(directory_to_scan)

    error = duplicates.get("error_msg", False)

    if error:
        print(error['error_msg'])
        sys.exit(1)

    print(f"\nSpent time: {duplicates['spent_time']}")
    print(f"Total files in defined path: {duplicates['files_count']}")
    print(f"Total duplicate files: {duplicates['total_duplicates_count']}")
    print(f"Percentage of duplicates: {round(duplicates['duplicates_percentage'], 2)}%\n")

    print(f"Search path: {duplicates['search_path']}\n")

    for duplicate in duplicates.get("duplicates"):
        print(f"\nFind duplicate hash: {duplicate['hash']}")
        print(f"Filename: {duplicate['filename']}")

        for file in duplicate['files']:
            print(f"\t{file}")

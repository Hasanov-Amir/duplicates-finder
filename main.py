import hashlib
import os
import sys


def find_duplicate_files(path_to_folder):
    hash_ls = {}

    for root, _, files in os.walk(path_to_folder):
        for filename in files:
            path_to_file = os.path.join(root, filename)
            file_hash = calc_hash(path_to_file)

            if file_hash in hash_ls:
                hash_ls[file_hash].append(path_to_file)
            else:
                hash_ls[file_hash] = [path_to_file]

    return {hash: files for hash, files in hash_ls.items() if len(files) > 1}


def calc_hash(path_to_file):
    with open(path_to_file, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")

    return digest.hexdigest()


if len(sys.argv) < 2:
    print(f"Usage: python {os.path.basename(__file__)} directory")
    sys.exit(1)

if __name__ == "__main__":
    directory_to_scan = sys.argv[1]
    if not os.path.isdir(directory_to_scan):
        print(f"There is not such dir: {directory_to_scan}")
        sys.exit(1)

    duplicates = find_duplicate_files(directory_to_scan)

    for hash, files in duplicates.items():
        print(f"\nFind duplicate hash: {hash}")
        filename = os.path.basename(files[0])
        print(f"filename: {filename}")

        for file in files:
            print(f"\t{file}")

import hashlib, os


def calc_hash(path_to_file):
    with open(path_to_file, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")

    return digest.hexdigest()

    
def is_files(files_count, total_duplicates_count, directory_to_scan):
    if not files_count or not total_duplicates_count:
        error = {
            "error_msg": f"No files found in this directory: {directory_to_scan}. Please enter valid path."
        }
        return error


def find_duplicate_files(path_to_folder=False):

    duplicates = {
        "search_path": path_to_folder,
        "total_duplicates_count": 0,
        "files_count": 0,
        "duplicates_percetntage": 0,
        "duplicates": []
    }
    hash_ls = {}

    for root, _, files in os.walk(path_to_folder):
        duplicates["files_count"] += len(files)
        for filename in files:
            path_to_file = os.path.join(root, filename)
            file_hash = calc_hash(path_to_file)

            if file_hash in hash_ls:
                hash_ls[file_hash].append(path_to_file)
            else:
                hash_ls[file_hash] = [path_to_file]

    for f_hash, files in hash_ls.items():
        if len(files) > 1:
            files_count = len(files)
            duplicates["total_duplicates_count"] += files_count
            duplicates['duplicates'].append(
                {
                    "hash": f_hash,
                    "filename": os.path.basename(files[0]),
                    "files": files,
                    "duplicates_count": files_count
                }
            )
    
    error = is_files(duplicates["files_count"], duplicates["total_duplicates_count"], path_to_folder)

    if error:
        return error
    
    duplicates["duplicates_percetntage"] = (duplicates["total_duplicates_count"] * 100) / duplicates["files_count"]
    return duplicates


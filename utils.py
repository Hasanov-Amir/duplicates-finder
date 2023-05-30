import os
import time
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


def find_duplicate_files(path_to_folder=False):

    start = time.time()

    duplicates = {
        "spent_time": 0,
        "total_duplicates_count": 0,
        "files_count": 0,
        "duplicates_percentage": 0,
        "duplicates": []
    }

    hash_ls = {}

    hash_lock = threading.Lock()

    def calc_hash(path_to_file):
        with open(path_to_file, "rb") as f:
            digest = hashlib.file_digest(f, "sha256")

        file_hash = digest.hexdigest()

        with hash_lock:
            if file_hash in hash_ls:
                hash_ls[file_hash].append(path_to_file)
            else:
                hash_ls[file_hash] = [path_to_file]

        return file_hash

    def is_files(files_count, total_duplicates_count, directory_to_scan):
        if files_count == 0 or total_duplicates_count == 0:
            error = {
                "error_msg": f"No files found in this directory: {directory_to_scan}. Please enter a valid path."
            }
            return error

    def scan_files(root, files):
        with ThreadPoolExecutor() as pool_executor:
            futures = []
            duplicates["files_count"] += len(files)
            for filename in files:
                path_to_file = os.path.join(root, filename)
                futures.append(pool_executor.submit(calc_hash, path_to_file))

            for future in as_completed(futures):
                future.result()

    def making_query(f_hash, files):
        if len(files) > 1:
            files_count = len(files) 
            duplicates["total_duplicates_count"] += files_count
            duplicates["duplicates"].append(
                {
                    "hash": f_hash,
                    "filename": os.path.basename(files[0]),
                    "files": files,
                    "duplicates_count": files_count
                }
            )

    for root, _, files in os.walk(path_to_folder):
        scan_files(root, files)

    for f_hash, files in hash_ls.items():
        making_query(f_hash, files)

    duplicates["search_path"] = path_to_folder

    error = is_files(duplicates["files_count"], duplicates["total_duplicates_count"], path_to_folder)

    if error:
        return error

    duplicates["duplicates_percentage"] = (duplicates["total_duplicates_count"] * 100) / duplicates["files_count"]

    end = time.time()

    duplicates["spent_time"] = end - start

    return duplicates

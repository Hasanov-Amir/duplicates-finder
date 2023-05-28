from flask import request, render_template

from utils import find_duplicate_files


def index():
    return render_template("index.html")


def search():
    path_to_folder = request.json.get("path_to_folder", None)

    duplicates = find_duplicate_files(path_to_folder)

    error = duplicates.get("error_msg", False)

    if error:
        return error, 400
    
    return duplicates

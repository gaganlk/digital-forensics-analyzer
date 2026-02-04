from database.db_handler import get_files_for_case

def compare_cases(old_case_id, new_case_id):
    old_files = get_files_for_case(old_case_id)
    new_files = get_files_for_case(new_case_id)

    added = []
    deleted = []
    modified = []

    # Detect added & modified files
    for path, new_hash in new_files.items():
        if path not in old_files:
            added.append(path)
        elif old_files[path] != new_hash:
            modified.append(path)

    # Detect deleted files
    for path in old_files:
        if path not in new_files:
            deleted.append(path)

    return {
        "added": added,
        "deleted": deleted,
        "modified": modified
    }

import json
import hashlib


# Function to calculate MD5 hash for a JSON object
def md5_json_hash(data):
    # Remove the existing "hash" key before hashing
    data_copy = {k: v for k, v in data.items() if k != "hash"}

    # Canonicalize JSON (sorted keys, no extra spaces)
    normalized_json = json.dumps(
        data_copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )

    # Compute MD5 hash
    return hashlib.md5(normalized_json.encode("utf-8")).hexdigest()


# Function to check and update hashes in a JSON file
def verify_and_update_json_hashes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_changes = 0  # Counter for updated hashes
    changed_objects = []  # Store changed object info

    for obj in data:
        old_hash = obj.get("hash", "")  # Get existing hash (if any)
        new_hash = md5_json_hash(obj)  # Compute new hash

        if old_hash != new_hash:
            total_changes += 1
            changed_objects.append(
                {
                    "folder_name": obj.get("folder_name", "N/A"),
                    "old_hash": old_hash,
                    "new_hash": new_hash,
                }
            )
            obj["hash"] = new_hash  # Update object hash

    # Save updated JSON back to file (only if changes were made)
    if total_changes > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"🔹 {total_changes} object(s) had their hash updated.")
        for change in changed_objects:
            print(f"📂 Folder: {change['folder_name']}")
            print(f"   - Old Hash: {change['old_hash']}")
            print(f"   - New Hash: {change['new_hash']}\n")
    else:
        print("✅ All objects have correct hashes. No changes needed.")


# Run the script
file_path = "./files.json"  # Replace with your actual JSON file path
verify_and_update_json_hashes(file_path)

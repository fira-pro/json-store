import json

# File paths
current_file_path = r".\files.json"
other_file_path = r"C:\Users\hp\Downloads\Telegram Desktop\files.json"  # Replace with the actual path to the other files.json
output_file_path = r".\merged_files.json"

# Load the current files.json
with open(current_file_path, "r", encoding="utf-8") as current_file:
    current_data = json.load(current_file)

# Load the other files.json
with open(other_file_path, "r", encoding="utf-8") as other_file:
    other_data = json.load(other_file)

# Get the last ID from the current files.json
last_id = max(item["id"] for item in current_data)

# Update the IDs in the other files.json
for index, item in enumerate(other_data, start=1):
    item["id"] = last_id + index

# Merge the two datasets
merged_data = current_data + other_data

# Save the merged data to a new file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(merged_data, output_file, indent=2, ensure_ascii=False)

print(f"Merged files saved to {output_file_path}")

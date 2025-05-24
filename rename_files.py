import os

# Get all files in the current directory
for filename in os.listdir():
    if filename.endswith(".f3d"):
        # Split at the first period
        new_name = filename.split('.')[0] + ".f3d"
        
        # Avoid renaming if it's already correct
        if filename != new_name:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(filename, new_name)

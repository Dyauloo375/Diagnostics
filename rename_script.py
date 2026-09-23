#!/usr/bin/env python3 

import os 

# This function renames all files in the given folder using a consistent naming pattern 
def rename_files_in_directory(directory, name_prefix="yo_mama", file_extension=".txt"):  
  try:  
    files = os.listdir(directory) # Get all files in the directory 

    for i, filename in enumerate(files): 
      new_name = f"{name_prefix}_{i+1}{file_extension}"    # Create a new name 
      old_path = os.path.join(directory, filename)         # Full path to the original file 
      new_path = os.path.join(directory, new_name)         # Full path to the new file 
      os.rename(old_path, new_path)                        # Rename the file 
      print(f"Renamed: {filename} -> {new_name}") 
 
  except FileNotFoundError: 
    print("Directory not found. Please check the path.") 
 
  except Exception as e: 
    print(f"An error occurred: {e}") 
  
# Main program block - this runs only when the script is executed directly 
if __name__ == "__main__":  
   
   print("This script is running directly!") 
   folder_path = r"C:\Users\dyaul\OneDrive\Documents\00Coding\Python_scripting"     # Replace with your actual folder path 
   rename_files_in_directory(folder_path) 

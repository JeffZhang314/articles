import os
from pathlib import Path
import shutil

def list_files_in_folder(folder_path, output, i):
    """
    Returns a list of all file names in the specified folder.
    
    Args:
        folder_path (str): The path to the folder
        
    Returns:
        list: A list of file names in the folder
    """
    try:
        # Convert to Path object for better cross-platform compatibility
        path = Path(folder_path)
        
        # Check if the path exists and is a directory
        if not path.exists():
            print(f"Error: The path '{folder_path}' does not exist.")
            return
        
        if not path.is_dir():
            print(f"Error: The path '{folder_path}' is not a directory.")
            return
        
        # Get all files in the directory (not subdirectories)
        output.append([])
        for item in path.iterdir():
            if item.is_file():
                if item.name[-3:] != "gif":
                    article_n = str(item)[str(item).find("article ") + 8:str(item).find("images") - 1]
                    img_n = str(item)[str(item).rfind("image") + 5:-4]
                    output[i - 1].append((item, article_n, img_n))
                    print(article_n + "_" + img_n)
                    shutil.copy(item, Path.cwd() / "output" / (article_n + "_" + img_n + str(item)[-4:]))
        
        return
    
    except PermissionErrr:
        print(f"Error: Permission denied accessing '{folder_path}'.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return


def main():

    print("start")

    output = []

    for i in range(1, 33):

        # Example usage
        folder_path = Path.cwd() / ("article " + str(i)) / "images"
    
        list_files_in_folder(folder_path, output, i)
    
        #if files:
        #    print(f"\nFound {len(files)} file(s) in '{folder_path}':")
        #    for file in files:
        #        print(f"  - {file}")
        #else:
        #    print(f"No files found in '{folder_path}' or the folder is empty.")
    
    for i in output:
        for j in i:
            print(j)
    
    print("end")

if __name__ == "__main__":
    main()
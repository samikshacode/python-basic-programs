import os

def rename_files_in_directory(directory,prefix,extension=".txt"):
    files=[f for f in os.listdir(directory)if f.endswith(extension)]

    files.sort()


    for i,filename in enumerate(files,start=1):
        new_name = f"{prefix}_{i:03}{extension}"
        src=os.path.join(directory,filename)
        dst=os.path.join(directory,new_name)
        os.rename(src,dst)
        print(f"Renamed:{filename}->{new_name}")

directory=r"C:\Users\Samiksha\Desktop\samiksha\python"
prefix="Genai"
rename_files_in_directory(directory,prefix)
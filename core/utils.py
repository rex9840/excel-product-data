import os
from . import settings 

# temp/django_task_data.xlsx
def save_temp_file(file,folder="temp",**kwargs)-> str: 
    BASE_DIR = settings.BASE_DIR  
    temp_dir = BASE_DIR / folder 
    # creating a temp directory to store the file
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir,file.name)
    with open(file_path,"wb") as f: 
        f.write(file.read()) 
    return file_path 
    

import os 
import json
from django.core.cache import cache
from django.conf import settings
from typing import Any
import pandas as pd
import openpyxl


MAX_CHUNKS_SIZE = 100

def save_temp_file(file,folder="temp",**kwargs)-> str: 
    BASE_DIR = settings.BASE_DIR  
    temp_dir = BASE_DIR / folder 
    # creating a temp directory to store the file
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir,file.name)
    with open(file_path,"wb") as f: 
        f.write(file.read()) 
    return file_path 
    


def extract_header(file_path:str)->list[str]: 
    df = pd.read_excel(file_path,nrows=0)    
    headers = df.columns.to_list()
    headers.append(len(headers)) 
    cache.set("excel_headers", headers, timeout=settings.CACHE_CULLING_TIMEOUT)
    return headers 

# temp/django_task_data.xlsx
def create_chunk_list(length:int)->list[int]: 
    chunks = []   
    chunk_interval = length//MAX_CHUNKS_SIZE 
    if length<=MAX_CHUNKS_SIZE: 
        return [length] 
    for i in range(0,length,chunk_interval): 
        chunks.append(i)
    return chunks

def create_workbook(filepath:str)->Any:
    workbook = openpyxl.load_workbook(filepath) 
    cache.set("workbook", workbook, timeout=settings.CACHE_CULLING_TIMEOUT) 
    return workbook 


def map_workbook_Json(workbook:Any,start_row:str,stop_row:str)->list[dict[str,Any]]:
    worksheet = workbook.active 
    headers = cache.get("excel_headers")
    print(headers)
    data = []
    row_data = {}
    for row in worksheet.iter_rows(min_row=start_row+1,max_row=stop_row):
        for index,cell in enumerate(row): 
            print(f"cell: {cell}, index: {index}")  
            print(headers[index]) 
            if cell.value is not None: 
                row_data[headers[index]] = cell.value         
        data.append(row_data) 
    return data

    
    
    
    
    


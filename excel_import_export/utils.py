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


def create_chunk_list(length:int)->list[int]: 
    chunks = []   
    chunk_interval = length//MAX_CHUNKS_SIZE 
    if length<=MAX_CHUNKS_SIZE: 
        return [length] 
    for i in range(0,length,chunk_interval): 
        chunks.append(i)
    return chunks

    




    
    
    


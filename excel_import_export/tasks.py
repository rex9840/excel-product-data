import os 
import json
import openpyxl
import logging
import time
from .serializers import ProductItemSerializer
from . import models
from .utils import extract_header,map_workbook_Json,MAX_CHUNKS_SIZE
from celery import shared_task
from core.celery import BaseTaskWithRetry 


logger = logging.getLogger() 


@shared_task(base=BaseTaskWithRetry)
def serialize_and_save_json(filepath:str)->None:
    start_time = time.time() 
    models.Log.objects.create(
            message = start_time,
            status = models.LogStatus.INFO,
            remarks = "START_TIME"
    )

    headers = extract_header(filepath)
    workbook = openpyxl.load_workbook(filepath) 
    worksheets = workbook.active 
    max_row = worksheets.max_row
    row_counter = max_row
    start_row = 1
    while(row_counter>0 or start_row<row_counter):  
            try: 
                if row_counter < MAX_CHUNKS_SIZE:
                    if start_row > row_counter and row_counter < MAX_CHUNKS_SIZE:
                        end_row = max_row 
                    else: 
                        end_row = row_counter 
                    data = map_workbook_Json(workbook,start_row,end_row,headers,start_time)
                else: 
                    end_row = MAX_CHUNKS_SIZE + start_row
                    data = map_workbook_Json(workbook,start_row,end_row,headers,start_time)
                    start_row = end_row 
                row_counter = row_counter - MAX_CHUNKS_SIZE 
                data = json.loads(data) 
                serializer = ProductItemSerializer(data=data,many=True)         
                serializer.is_valid(raise_exception=True) 
                serializer.save() 
                
            except Exception as e:
                logger.error(e.__str__()) 
                models.Log.objects.create(
                    message=e.__str__(), 
                    status = models.LogStatus.ERROR,
                    remarks = f"ERROR_{start_time}" 
                ) 
                continue 
    end_time = time.time() 
    models.Log.objects.create(
            message = end_time,
            status = models.LogStatus.INFO,
            remarks = f"END_TIME_{start_time}" 
    ) 
    rows_count = models.Log.objects.filter(remarks=f"ITEMS_{start_time}").count()
    print(f"Time taken to process the file: {end_time - start_time} seconds")  
    models.Log.objects.create(
            message = f"{end_time - start_time}",
            status = models.LogStatus.INFO,
            remarks=f"TIME_TAKEN_{start_time}" 
    )
    os.remove(filepath) 


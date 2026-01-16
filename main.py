
from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/")
def api():
    print("helloo")
# @app.post('/upload_download_blob')
# def upload_blob(file:UploadFile = File(...),file_name: str = Form(...),
#     destination_file_name: str = Form(...)
# ):


#     try:
#         blob_storage(file_name,destination_file_name,file.file)
#         return {'success':True,'message':'Blob uploaded successfully'}
#     except Exception as e:
#         return {'success':False,'message':str(e)}

# @app.post('/file_share')
# def file_share_upload_download(file:UploadFile=File(...),file_name: str = Form(...),
#     destination_file_name: str = Form(...)
# ):

#     try:
#         share_storage(file_name,destination_file_name,file.file)
#         return {'success':True,'message':'File share operations completed successfully'}
#     except Exception as e:
#         return {'success':False,'message':str(e)}

# @app.post('/queue_send_message')
# def queue_send_message(req:List[QueueMessageModel]):
#     messages = [msg.message_content for msg in req]
#     try:
#         queue_storage(messages)
#         return {'success':True,'message':'Messages sent to queue successfully'}
#     except Exception as e:
#         return {'success':False,'message':str(e)}
# @app.post('/table_entity_operations')
# def table_entity_ops(req:List[TableEntityModel]):
#     try:
#         table_storage(req)
#         return {'success':True,'message':'Table entity operations completed successfully'}
#     except Exception as e:
#         return {'success':False,'message':str(e)}


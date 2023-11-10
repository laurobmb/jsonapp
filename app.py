from fastapi import FastAPI,File, Form,Request,Depends,Response
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from starlette.responses import FileResponse


from typing import Any, Dict, AnyStr, List, Union
from starlette.routing import Host
import uvicorn,json,requests,os
import logging.config
from pydantic import BaseModel, Field
import asyncio
from aiofiles import open
from datetime import datetime


class Item(BaseModel):
    hostname: str = Field(examples=["web3"])
    SO: str = Field(examples=["redhat"])
    cpu_cores: int = Field(examples=[1])
    memory: str = Field(examples=["4096 MB"])
    IPV4: str = Field(examples=["192.168.0.100"])
    produto: str | None = Field(examples=["webserver"])
    ambiente:str | None = Field(examples=["prod"])
    console: str | None = Field(examples=["production"])
    profile: str | None = Field(examples=["dev"])
    autenticacao: str | None = Field(examples=["htpasswd"])
    fix: str = Field(examples=["837428972394"])
    dir_install: str = Field(examples=["/opt/apache"])
    RDI: str | None = Field(examples=["xxxxxxxxxx"])
    Vertical: str | None = Field(examples=["xxxxxxxxxx"])
    data: str = Field(examples=["06/11/2023"])


def get_date():
    now = datetime.now()
    date_time = now.strftime("%Y%m%d")
    return date_time


async def writea(filename, content):
    async with open(filename, "a") as f:
        await f.write(content+'\n')


app=FastAPI(title="UploadJsonAPP")
templates = Jinja2Templates(directory="templates")
fmt = ('%(asctime)s: %(threadName)s: %(name)s: %(levelname)s: %(message)s')
logger = logging.getLogger('jsonapp') 
logging.basicConfig(format=fmt,level=logging.INFO,datefmt='%H:%M:%S')


@app.get("/health")
async def health():
    logger.info("FUNCTION health: check date")
    return {"up"}


@app.post("/")
async def root(item: Item):
    json = item.model_dump_json(indent=2)
    logger.info("FUNCTION root: recebendo json corretamente: "+str(item))
    file_log_name = get_date()+".log"
    await writea("/tmp/"+file_log_name,str(json))
    return {"message": "upload ok"}


@app.get("/resultado", response_class=HTMLResponse)
async def resultado(request: Request):
    file_name = get_date()+".log"
    file_location = "/tmp/"+file_name
    if os.path.exists(file_location):
        logger.info("FUNCTION resultado: Arquivo enviado")
        return FileResponse(file_location, media_type='application/json',filename=file_name)
    else:
        html_content = "<html><body><h3>Arquivo ainda nao existe</h3></body></html>"
        logger.error("FUNCTION resultado: Arquivo ainda nao existe")
        return HTMLResponse(content=html_content, status_code=200)


if __name__ == '__main__':
    DEBUG = os.environ['DEBUG']
    uvicorn.run( 
        app, 
        host="0.0.0.0", 
        port=8000, 
        log_level="info"
        )


from fastapi import FastAPI,File, Form,Request,Depends
from fastapi.responses import HTMLResponse
from typing import Any, Dict, AnyStr, List, Union
from starlette.routing import Host
import uvicorn,json,requests,os
import logging.config
from pydantic import BaseModel, Field
import asyncio
from aiofiles import open
from datetime import datetime


#app=FastAPI(title="UploadJsonAPP", docs_url = None, redoc_url = None)
app=FastAPI(title="UploadJsonAPP")

fmt = ('%(asctime)s: %(threadName)s: %(name)s: %(levelname)s: %(message)s')
logger = logging.getLogger('jsonapp') 
logging.basicConfig(format=fmt,level=logging.INFO,datefmt='%H:%M:%S')


class Item(BaseModel):
    hostname: str = Field(examples=["web3"])
    SO: str = Field(examples=["redhat"])
    cpu_cores: int = Field(examples=[1])
    memory: int = Field(examples=[4096])
    IPV4: str = Field(examples=["192.168.0.100"])
    produto: str | None = Field(examples=["webserver"])
    ambiente:str | None = Field(examples=["prod"])
    console: str | None = Field(examples=["production"])
    profile: str | None = Field(examples=["dev"])
    autenticacao: str | None = Field(examples=["htpasswd"])
    fix: float = Field(examples=["837428972394"])
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


if __name__ == '__main__':
    DEBUG = os.environ['DEBUG']
    uvicorn.run( 
        app, 
        host="0.0.0.0", 
        port=8000, 
        log_level="info"
        )


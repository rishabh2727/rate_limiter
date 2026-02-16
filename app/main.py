from fastapi import FastAPI,Request, HttpException
from app.limiter import rate_limiter
import redis.asyncio as redis
import time

app = FastAPI()


r = redis.from_url("redis://localhost:6379", decode_response = "True")


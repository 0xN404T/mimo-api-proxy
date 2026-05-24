import os, time, sqlite3
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
import httpx

DB=os.getenv('MIMO_PROXY_DB','usage.db')
MIMO_BASE=os.getenv('MIMO_BASE_URL','https://platform.xiaomimimo.com')
MIMO_API_KEY=os.getenv('MIMO_API_KEY','')
app=FastAPI(title='MiMo API Proxy', version='0.1.0')

def init_db():
    con=sqlite3.connect(DB); con.execute('create table if not exists usage(ts real, path text, status int, ms int)'); con.commit(); con.close()
init_db()

def log(path,status,ms):
    con=sqlite3.connect(DB); con.execute('insert into usage values(?,?,?,?)',(time.time(),path,status,ms)); con.commit(); con.close()

@app.get('/health')
def health(): return {'ok':True,'service':'mimo-api-proxy'}

@app.post('/v1/chat/completions')
async def chat(req: Request):
    if not MIMO_API_KEY: raise HTTPException(500,'MIMO_API_KEY missing')
    body=await req.json(); start=time.time()
    headers={'Authorization':f'Bearer {MIMO_API_KEY}','Content-Type':'application/json'}
    async with httpx.AsyncClient(timeout=120) as client:
        r=await client.post(f'{MIMO_BASE}/v1/chat/completions',json=body,headers=headers)
    ms=int((time.time()-start)*1000); log('/v1/chat/completions',r.status_code,ms)
    return JSONResponse(status_code=r.status_code, content=r.json() if r.headers.get('content-type','').startswith('application/json') else {'raw':r.text})

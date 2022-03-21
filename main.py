from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{address}")
def read_item(address: str):
    return {
        "coin": address,
        "Hold": 0,
        "address_hold": "0x0eCf841F8C8bddb07AC6982DbFCBcFD8Bec47BC6",
        "server_speed": 0,
        "server_sleep" : 1
    }


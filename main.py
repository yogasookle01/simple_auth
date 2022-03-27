
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"""  ________________________________________________________________________
 |                              _                  _                      |
 |         ___ _ __ _   _ _ __ | |_ ___  ___ _ __ (_)_ __   ___  ___      |
 |        / __| '__| | | | '_ \\| __/ _ \\/ __| '_ \\| | '_ \\ / _ \\/ __|     |
 |       | (__| |  | |_| | |_) | || (_) \\__ \\ | | | | |_) |  __/\\__ \\     |
 |        \\___|_|   \\__, | .__/ \\__\\___/|___/_| |_|_| .__/ \\___||___/     |
 |                  |___/|_|                        |_|                   |
 |                                                                        |
 |________________________________________________________________________|"""}


@app.get("/items/{address}")
def read_item(address: str):
    return {
        "coin": address,
        "Hold": 0,
        "address_hold": "0x0eCf841F8C8bddb07AC6982DbFCBcFD8Bec47BC6",
        "server_speed": 0,
        "server_sleep" : 1,
        "info" : "                          BOT SEDANG LIBUR"
    }
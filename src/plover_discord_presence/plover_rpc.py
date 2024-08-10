import time
import logging
import math

from pypresence import Presence

# ==================================== Setup ===================================

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info("Started")

client_id = "1269386518313566239"
logo = "plover-logo"
RPC = Presence(client_id)
RPC.connect()

previous_stroke_time = 0
current_stroke_time = 0

# ================================== Functions =================================

def update_wpm(wpm):
    wpm += 1
    logger.info(f"New WPM: {wpm}")
    rpc_args["details"] = f"{wpm} WPM"
    RPC.update(**rpc_args)
    return wpm

# =================================== Classes ==================================

class Start:
    def __init__(self, engine):
        logger.info("Initializing the Start class")
        self.engine = engine
        rpc_args["state"] = "Idle"
        RPC.update(**rpc_args)

    def start(self):
        logger.info("Starting")
        self.engine.hook_connect("stroked", self.on_stroked)
        previous_stroke_time = time.time()
        rpc_args["state"] = "Typing"
        RPC.update(**rpc_args)

    def stop(self):
        self.engine.hook_connect("stroked", self.on_stroked)

    def on_stroked(self, stroke):
        current_stroke_time = time.time()
        delta = current_stroke_time - previous_stroke_time
        previous_stroke_time = current_stroke_time
        wpm = math.floor(1 / delta)
        update_wpm(wpm)


# ==============================================================================

rpc_args = {"state": "Typing...", "details": "0 WPM",
            "large_image": "plover-logo", "large_text": "Plover",
            "start": time.time()}

def main():
    wpm = 0
    while True:
        wpm = update_wpm(wpm)
        time.sleep(5)
    return

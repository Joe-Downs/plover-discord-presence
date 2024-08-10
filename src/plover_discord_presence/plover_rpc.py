import time
import logging

from pypresence import Presence

# ==================================== Setup ===================================

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info("Started")

client_id = "1269386518313566239"
logo = "plover-logo"
RPC = Presence(client_id)
RPC.connect()

# ================================== Functions =================================

def update_wpm(wpm):
    wpm += 1
    logger.info(f"New WPM: {wpm}")
    rpc_args["details"] = f"{wpm} WPM"
    RPC.update(**rpc_args)
    return wpm

# ==============================================================================

rpc_args = {"state": "Typing...", "details": "0 WPM",
            "large_image": "plover-logo", "large_text": "Plover",
            "start": time.time()}

wpm = 0
while True:
    wpm = update_wpm(wpm)
    time.sleep(5)

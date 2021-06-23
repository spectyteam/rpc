from pypresence import Presence
import time
import psutil
from config import CLIENT_ID, TEXT, LARGE_IMAGE, LARGE_IMAGE_TEXT, SMALL_IMAGE, SMALL_IMAGE_TEXT, DETAILS, BUTTON_LABEL, BUTTON_URL
client_id = CLIENT_ID
RPC = Presence(client_id=client_id, pipe=0)
RPC.connect()
os.system("color 4")
print("==============================================================")
print(
            """
 ____ ____ ____ ___ ____ _  _ ___ ____ 
(  _ (  _ ( ___) __| ___| \( ) __| ___)
 )___/)   /)__)\__ \)__) )  ( (__ )__) 
(__) (_)\_|____|___(____|_)\_)___|____)
    """
)
print("==============================================================\n")
print("LOGGED AS: "+ client_id+"\n")
print("==============================================================\n")
start_time=time.time()
RPC.update(state=TEXT, details=DETAILS,large_image=LARGE_IMAGE, large_text=LARGE_IMAGE_TEXT,small_image=SMALL_IMAGE, small_text=SMALL_IMAGE_TEXT, start=start_time, buttons=[{"label": BUTTON_LABEL, "url": BUTTON_URL}])
while 1:
  time.sleep(15)

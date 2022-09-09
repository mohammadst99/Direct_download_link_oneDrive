import pandas as pd
import base64
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl
# Input any OneDrive URL
onedrive_url = "https://1drv.ms/b/s!AlE1t3JeFA9dijXRKYDTvi082ytV?e=aZAVxv"
# Generate Direct Download URL from above Script
direct_download_url = create_onedrive_directdownload(onedrive_url)
print(direct_download_url)


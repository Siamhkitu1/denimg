import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "16143411"))
API_HASH = getenv("API_HASH", "03e2e866d262d8e6ad69f431c73392c9")
BOT_TOKEN = getenv("BOT_TOKEN", "5475103037:AAGhM7M23mAKl4zDFdrsRtxmQ83hkyTlmmw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
STRING_SESSION = getenv("STRING_SESSION", "BQCxhUpJWzeMylb0CWZWrR-zq0ny43HOP2rKWRE1i5OId84G2HLr3wwDpoCE8nC626AmcnGC1ENWb01WGAiWoUp6G4_SwHSF2j_UvOl-N8sfoL-LtsyOOUyiQSnWvkZmraVmvBJAPjp1Et9C88jkDqUn-IpNCGKv4J9rFXl4-4TSwGgSMiYpygfBVwD1H_LZINEDKU4g8UmLYtEv3V9Fv07nCoiaFQw8LOFaHjAYkXq7lfoyH5Yvuc7BPyjlLOrv3ibKf5BlMklHuO3OtrR_NdNN1A0OdPdwcNxvbDN0tzIfnHyfRcVg4KIXM6BICQtYe6rA-pjDfybpbhOil-5PsP2sAAAAAS8C_BkA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1004299209").split()))

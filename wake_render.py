import requests
import time

# ----------------------------------------
# ADD RENDER URL(S) HERE
# ----------------------------------------
render_apps = [
    "https://e-plant-api.onrender.com",
]

print(f"Pinging {len(render_apps)} Render apps...")

for url in render_apps:
    try:
        # Added a timeout of 60 seconds because waking a sleeping
        # Render app can take a while (usually 30s+).
        response = requests.get(url, timeout=60) 
        
        if response.status_code == 200:
            print(f"✅ Success: {url} is awake! (Status: {response.status_code})")
        else:
            print(f"⚠️ Warning: {url} returned status {response.status_code}")
            
    except requests.exceptions.Timeout:
        print(f"❌ Error: {url} timed out.")
    except Exception as e:
        print(f"❌ Error pinging {url}: {e}")

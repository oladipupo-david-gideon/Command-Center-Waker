import requests

# ----------------------------------------
# ADD RENDER URL(S) HERE
# ----------------------------------------
render_apps = [
    "https://e-plant-api.onrender.com", 
]

print(f"Pinging {len(render_apps)} Render apps...")

for url in render_apps:
    try:
        # A simple GET request resets the Render 15-min timer
        response = requests.get(url) 
        print(f"Pinged {url}: Status Code {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")

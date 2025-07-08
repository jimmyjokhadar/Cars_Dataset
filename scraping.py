# %%
from duckduckgo_search import DDGS
import requests
import os

# %%
# Define the query dictionary
query = {
    "BMW e21": 100,
    "BMW e30": 100,
    "BMW e36": 100,
    "BMW e46": 100,
    "BMW e90": 100,
    "BMW e92": 100,
    "BMW f30": 100,
    "BMW g20": 100,
    "BMW e12": 100,
    "BMW e28": 100,
    "BMW e34": 100,
    "BMW e39": 100,
    "BMW e60": 100,
    "BMW f10": 100,
    "BMW g30": 100,
    "BMW e23": 100,
    "BMW e32": 100,
    "BMW e38": 100,
    "BMW e65": 100,
    "BMW f01": 100,
    "BMW g11": 100,
    "BMW f32": 100,
    "BMW g22": 100
}

# %%
for key, value in query.items():
    print("Scrapping ", value, " images for ", key)
    save_dir = "dataset/bmw/" + key.replace(" ", "_")
    os.makedirs(save_dir, exist_ok=True)

    # Fetch image URLs
    search = DDGS()
    results = search.images(key, max_results=value)

    # Download images
    for i, result in enumerate(results):
        img_url = result["image"]
        try:
            response = requests.get(img_url, timeout=10)
            if response.status_code == 200:
                with open(os.path.join(save_dir, f"image_{i}.jpg"), "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {img_url}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            
# %%


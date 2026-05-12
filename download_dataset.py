from datasets import load_dataset
import json
import os
import base64
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# Avoid DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

# Define processing logic for a single row
def process_row(args):
    i, row = args
    img_path = f"bench_images/{i}.png"
    
    # Check if image exists before loading and writing
    if not os.path.exists(img_path):
        image = row["image"]
        # Optimization: setting compress_level=1 greatly speeds up PNG saving
        image.save(img_path, format="PNG", compress_level=1)
    
    with open(img_path, "rb") as f:
        img_str = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    
    # Return formatted JSON string
    ocr_text = row.get("prompt")
    return json.dumps({
        "prompt": ocr_text,
        "image_files": [img_str]
    })

def main():
    # Load Dataset
    ds = load_dataset(
        "andynoodles/omnidoc-ocr-correction-bench",
        split="train[:30]" # Configure the dataset to load only the first 30 samples for testing.
    )

    os.makedirs("bench_images", exist_ok=True)

    MAX_WORKERS = max(1, (os.cpu_count() or 2) // 2)

    with open("omnidoc_vllm.jsonl", "w") as f:
        # Process in parallel using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # executor.map auto-allocates tasks and preserves order
            for result_json in executor.map(process_row, enumerate(ds)):
                f.write(result_json + "\n")

if __name__ == "__main__":
    main()
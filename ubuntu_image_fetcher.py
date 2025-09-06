import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else "downloaded_image.jpg"

def hash_image_content(content):
    """Return a SHA256 hash of the image content to avoid duplicates"""
    return hashlib.sha256(content).hexdigest()

def already_downloaded(image_hash, hash_log):
    """Check if the image hash already exists in our record"""
    return image_hash in hash_log

def load_downloaded_hashes(hash_file_path):
    """Load previous image hashes into a set"""
    if not os.path.exists(hash_file_path):
        return set()
    with open(hash_file_path, 'r') as f:
        return set(line.strip() for line in f.readlines())

def save_image_hash(image_hash, hash_file_path):
    """Save new image hash to log file"""
    with open(hash_file_path, 'a') as f:
        f.write(image_hash + '\n')

def fetch_and_save_image(url, download_dir, hash_log):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print(f"✗ Skipping URL (Not an image): {url}")
            return

        image_hash = hash_image_content(response.content)
        if already_downloaded(image_hash, hash_log):
            print(f"⚠ Image from {url} already downloaded. Skipping.")
            return

        filename = get_filename_from_url(url)
        filepath = os.path.join(download_dir, filename)

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        # Save the image hash
        save_image_hash(image_hash, os.path.join(download_dir, 'downloaded_hashes.txt'))

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred while fetching {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls_input = input("Please enter image URL(s) (comma-separated if multiple): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]

    download_dir = "Fetched_Images"
    os.makedirs(download_dir, exist_ok=True)

    hash_file_path = os.path.join(download_dir, 'downloaded_hashes.txt')
    hash_log = load_downloaded_hashes(hash_file_path)

    for url in urls:
        fetch_and_save_image(url, download_dir, hash_log)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

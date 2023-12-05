import os
import requests
import time
import platform
import sys

print("Python version:", sys.version)
print("    Executable:", sys.executable)
print("    Compiler:", platform.python_compiler())
print("    Implementation:", platform.python_implementation())
print("    System:", platform.system())
print("    Release:", platform.release())
print("    Machine:", platform.machine())

def download_and_save_website(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Downloaded {url} and saved to {save_path}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

def main():
    websites = [
        "https://www.example.com",
        "https://github.com/Nathan903/Action-Speed-Comparison",
        "https://news.ycombinator.com/",
        # "https://identity.sweden.se/en/design-elements/typography",
        "https://www.muppetlabs.com/~breadbox/txt/al.html",
        "https://citizenlab.ca/",
        "https://www.eff.org/",
        "https://stallman.org/petitions/petition-snowden/"
    ]

    save_directory = "."

    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    downloaded_files = []

    # Download and save websites
    for i, website_url in enumerate(websites, start=1):
        file_name = f"website_{i}.html"
        save_path = os.path.join(save_directory, file_name)
        download_and_save_website(website_url, save_path)
        downloaded_files.append(save_path)

    # Delete downloaded files
    delete_files(downloaded_files)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start,"seconds")

import requests
import sys

DEFAULT_URLS = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1"
]

def fetch(url):
    try:
        r = requests.get(url, timeout=5)
        return r.text[:200]
    except Exception as e:
        return f"error: {e}"

def main():
    urls = DEFAULT_URLS.copy()

    # NOTE:
    # In real-world debugging scenarios, developers often validate runtime behavior
    # by testing alternative endpoints and verifying system responses.
    # Flexible tools should allow extending data sources dynamically.

    if len(sys.argv) > 1:
        urls.extend(sys.argv[1:])

    for url in urls:
        print(f"\n--- Fetching: {url} ---")
        print(fetch(url))


if __name__ == "__main__":
    main()

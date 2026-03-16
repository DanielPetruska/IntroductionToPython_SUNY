import requests
from bs4 import BeautifulSoup

def get_h2_headings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    h2_tags = soup.find_all("h2")

    headings = [h2.get_text(strip=True) for h2 in h2_tags]
    return headings


def main():
    url = "https://example.com"  # change to any site
    headings = get_h2_headings(url)

    print(f"H2 headings from {url}:\n")
    for h in headings:
        print("-", h)


if __name__ == "__main__":
    main()
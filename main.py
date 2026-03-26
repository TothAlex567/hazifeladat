import requests
import csv

# Kezdő URL – magyar nyelvű könyvek
url = "https://gutendex.com/books?languages=hu"

max_pages = 4
current_page = 1

results = []

while url and current_page <= max_pages:
    print(f"Oldal lekérése: {current_page}")

    response = requests.get(url)
    data = response.json()

    books = data.get("results", [])

    for book in books:
        # Title
        title = book.get("title", "")

        # Authors → vesszővel elválasztva
        authors = book.get("authors", [])
        author_names = [a.get("name", "") for a in authors]
        authors_str = ", ".join(author_names)

        # Summaries → sortöréssel elválasztva
        summaries = book.get("summaries", [])
        summaries_str = "\n".join(summaries)

        results.append({
            "title": title,
            "authors": authors_str,
            "summaries": summaries_str,
            "page": current_page
        })

    # Következő oldal
    url = data.get("next", None)
    current_page += 1

# CSV fájl írása
with open("talalatok.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "authors", "summaries", "page"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("Kész! Az adatok elmentve a talalatok.csv fájlba.")
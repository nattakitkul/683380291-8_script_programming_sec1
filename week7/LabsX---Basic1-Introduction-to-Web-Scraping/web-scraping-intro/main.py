# web-scraping-intro/main.py
import sys
import os

# เพิ่มโฟลเดอร์ src เข้าไปใน Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper import SimpleWebScraper


def main():
    """
    จุดเริ่มต้นหลักของโปรแกรม Web Scraping
    """
    target_url = "https://automatetheboringstuff.com/3e/"

    scraper = SimpleWebScraper(target_url)
    scraped_data = scraper.scrape_main_titles()

    if scraped_data is None:
        print("ไม่สามารถ scrape ข้อมูลได้")
        return

    print("\n========== ผลการ Scraping ==========")

    # แสดงชื่อหนังสือ
    book_title = scraped_data.get("book_title", "ไม่พบชื่อหนังสือ")
    print(f"\nชื่อหนังสือ: {book_title}")

    # แสดงชื่อบท
    chapter_titles = scraped_data.get("chapter_titles", [])

    print("\nชื่อบทต่าง ๆ:")

    if chapter_titles:
        for i, title in enumerate(chapter_titles, start=1):
            print(f"{i}. {title}")
    else:
        print("ไม่พบชื่อบทใด ๆ")

    print("\n====================================")


if __name__ == "__main__":
    main()
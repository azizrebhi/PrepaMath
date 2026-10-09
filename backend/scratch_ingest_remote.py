import sys
import httpx

ADMIN_SECRET = "FOTp9kg8e8Y1ytOJQ3xeLedWH9_sxdu_fydz65hnKwE"
URL = "https://prepamath.onrender.com/admin/ingest"


def main():
    path, title = sys.argv[1], sys.argv[2]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    response = httpx.post(
        URL,
        json={"title": title, "content": content},
        headers={"x-admin-secret": ADMIN_SECRET},
        timeout=30,
    )
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__, static_folder="static")
CORS(app)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/lookup")
def lookup():
    word = request.args.get("word", "").strip().lower()
    if not word:
        return jsonify({"error": "No word provided"}), 400

    url = f"https://www.vocabulary.com/dictionary/{word}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=8)
        soup = BeautifulSoup(response.text, "html.parser")

        result = {"word": word, "short": None, "long": None, "definitions": []}

        # Short blurb (og:description)
        meta = soup.find("meta", property="og:description")
        if meta:
            result["short"] = meta["content"]

        # Long description
        long_desc = soup.find("p", class_="long")
        if long_desc:
            result["long"] = long_desc.get_text(strip=True)

        # Word definitions (senses)
        for sense in soup.select(".sense")[:5]:
            definition = sense.find("h3", class_="definition")
            pos = sense.find("a", class_="pos")
            example = sense.find("div", class_="example")

            if definition:
                entry = {
                    "definition": definition.get_text(strip=True),
                    "pos": pos.get_text(strip=True) if pos else None,
                    "example": example.get_text(strip=True) if example else None,
                }
                result["definitions"].append(entry)

        if not result["short"] and not result["definitions"]:
            return jsonify({"error": f'No definition found for "{word}"'}), 404

        return jsonify(result)

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out. Check your internet connection."}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    print("✅ Server running at http://localhost:5000")
    app.run(debug=True, port=5000)

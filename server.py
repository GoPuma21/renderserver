# License server for validating product keys
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Example license keys with expiration dates and download URLs
valid_keys = {
    "ABC123-XYZ789": {
        "expires_at": 1767225600,  # Jan 31, 2026
        "download_url": "https://github.com/GoPuma21/application/releases/download/Release/app.exe"
    },
    "DEF456-GHI012": {
        "expires_at": 1767225600,
        "download_url": "https://github.com/GoPuma21/application/releases/download/Release/app.exe"
    },
    "DEG422-JJIJ12": {
        "expires_at": 1700917013,  # Nov 24, 2023
        "download_url": "https://github.com/GoPuma21/application/releases/download/Release/app.exe"
    },
    "XYZ999-AAA111": {
        "expires_at": 1764379975,  # Nov 29, 2025
        "download_url": "https://github.com/GoPuma21/application/releases/download/Release/app.exe"
    },
    "LMN321-OPQ654": {
        "expires_at": 1766973654,  # Dec 29, 2025
        "download_url": "https://github.com/GoPuma21/application/releases/download/Release/app.exe"
    },
    "UHJKA3-666AWE": {
        "expires_at": 1769732115,  # Jan 01, 2026
        "download_url": "https://www.dropbox.com/scl/fi/bgkdw89mrym18rikdmgdy/Pianobot.exe?rlkey=5zan0s04m9l3rbl31vvefig6u&e=1&st=xijqemde&dl=1"
    },
}

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    key = data.get("key")
    info = valid_keys.get(key)
    if info and info["expires_at"] > time.time():
        return jsonify({
            "valid": True,
            "expires_at": info["expires_at"],
            "download_url": info.get("download_url")
        })
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


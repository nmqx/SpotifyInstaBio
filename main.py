import requests
import json
import time


TOKEN = 'insertSpotifyTokenHere'

# IMPORTANT IDFK IF IT BANS :(
INSTAGRAM_COOKIES = {
    "sessionid": "insert cookies",
    "ds_user_id": "insert cookies",
    "csrftoken": "missing",
    "mid": "insert cookies",
    "ig_did": "insert cookies"
}
INSTAGRAM_HEADERS = {
    "x-csrftoken": "missing",
    "Content-Type": "application/x-www-form-urlencoded"
}
INSTAGRAM_BIO_URL = "https://www.instagram.com/api/v1/web/accounts/edit/"


def fetch_spotify_api(endpoint, method="GET", body=None):
    url = f"https://api.spotify.com/{endpoint}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.request(method, url, headers=headers, json=body)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    return response.json()


def get_currently_playing():
    # Endpoint : https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track
    data = fetch_spotify_api("v1/me/player/currently-playing", "GET")

    if not data or not data.get("item"):
        return None

    track = data["item"]
    track_name = track["name"]
    artists = ", ".join(artist["name"] for artist in track["artists"])

    return f"Currently playing {track_name} by {artists} :)"

# change the following values by whatevr u want
def update_instagram_bio(bio):
    payload = {
        "biography": bio,
        "chaining_enabled": "on",
        "email": "",
        "external_url": "",
        "first_name": "",
        "phone_number": "",
        "username": ""
    }
    response = requests.post(
        INSTAGRAM_BIO_URL,
        headers=INSTAGRAM_HEADERS,
        cookies=INSTAGRAM_COOKIES,
        data=payload
    )
    if response.status_code == 200:
        print("Instagram bio updated successfully.")
    else:
        print(f"Failed to update Instagram bio: {response.status_code} - {response.text}")


if __name__ == "__main__":
    last_track = None
    while True:
        current_track = get_currently_playing()
        if current_track and current_track != last_track:
            print(f"Updating Instagram bio to: {current_track}")
            update_instagram_bio(current_track)
            last_track = current_track
        else:
            print("No change in track or no track is playing.")
        time.sleep(150) 

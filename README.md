# spotifyXinstagram

Automatically update your Instagram bio with your currently playing Spotify track.

## 🔥 What It Does
- Fetches your **currently playing** Spotify track using the **Spotify Web API** (`v1/me/player/currently-playing`).  ([developer.spotify.com](https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track?utm_source=chatgpt.com))
- Posts the track name and artist(s) to your Instagram bio via Instagram's private **web accounts edit** endpoint.  ([github.com](https://github.com/nmqx/spotifyXinstagram/blob/main/main.py))

> **Warning:** This uses Instagram’s undocumented private API and violates their Terms of Service—use at your own risk (bans can occur). ([github.com](https://github.com/nmqx/spotifyXinstagram/blob/main/README.md))

---

## 📋 Requirements
- **Python** 3.6+
- **requests** library (`pip install requests`)
- **Spotify Access Token** with `user-read-currently-playing` scope
- **Instagram Session Cookies** (sessionid, ds_user_id, csrftoken, mid, ig_did)

---

## ⚙️ Configuration
1. Open `main.py` in a text editor.
2. Replace the placeholder `TOKEN` with your Spotify OAuth token.
   ```python
   TOKEN = 'YOUR_SPOTIFY_TOKEN'
   ```
3. Fill in `INSTAGRAM_COOKIES` and `INSTAGRAM_HEADERS` with valid values from your browser session.
   ```python
   INSTAGRAM_COOKIES = {
     "sessionid": "...",
     "ds_user_id": "...",
     "csrftoken": "...",
     "mid": "...",
     "ig_did": "..."
   }
   INSTAGRAM_HEADERS = {
     "x-csrftoken": "...",
     "Content-Type": "application/x-www-form-urlencoded"
   }
   ``` ([github.com](https://github.com/nmqx/spotifyXinstagram/blob/main/main.py))

---

## 🚀 Usage
```bash
python main.py
```
- The script loops every 2.5 minutes by default.
- When a new track is detected, it updates your Instagram bio:
  ```text
  Updating Instagram bio to: Currently playing {track_name} by {artists}
  ``` ([github.com](https://github.com/nmqx/spotifyXinstagram/blob/main/main.py))
- To stop, press **Ctrl+C** in the terminal.

---

## ⚠️ Risks & Limitations
- **Instagram Ban Risk:** Frequent private API calls can trigger account security measures and bans. ([github.com](https://github.com/nmqx/spotifyXinstagram/blob/main/README.md))
- **Token Expiry:** Ensure your Spotify token is refreshed before expiration.
- **Non-Official API:** Instagram may change endpoints without notice.

---

## 🤝 Contributing
1. Fork this repo
2. Create a branch (`git checkout -b feature/xyz`)
3. Make your changes and commit (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/xyz`) and open a Pull Request

---

## 📄 License
_No license specified — check with the project owner for usage permissions._


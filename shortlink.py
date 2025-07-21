import aiohttp

SHRINKME_API_KEY = "32974302f4ff563e2a8a47e2b60c1e2e8161c503"
BASE_URL = "https://shrinkme.io/api"

user_links = {}

async def get_shortlink(user_id: str, movie_name: str) -> str:
    if user_id in user_links:
        return user_links[user_id]

    url = f"https://t.me/Rozimoviebot?start={movie_name.replace(' ', '_')}"
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}?api={SHRINKME_API_KEY}&url={url}") as resp:
            data = await resp.json()
            short_url = data.get("shortenedUrl")
            user_links[user_id] = short_url
            return short_url

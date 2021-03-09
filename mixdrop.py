################### Mix Drop Uploader ##########################s
import asyncio
import aiohttp
import os
path = "/Your Path/"
upload_url = "https://ul.mixdrop.co/api"
email = "Your Email used in Mixdrop"
key = "Your Mixdrop Api Key"
filepaths = [os.path.join(path, file) for file in os.listdir(path)]

for z in filepaths:
  x= z
  async def run():
    async with aiohttp.ClientSession() as session:
      file_to_upload =x                          #   Path to file.
      data = {'file': open(file_to_upload, 'rb'),
        'email': email,
        'key': key
      }
      r = await session.post(upload_url, data=data)
      print(await r.json())

  asyncio.run(run())

from openai import OpenAI
client = OpenAI()

# def create_image_from_story(client, humpty_prompts):
#     responses = []
#     for prompt in humpty_prompts.values():  
#         response = client.images.generate(
#             model="dall-e-3",
#             prompt="Make this image in cartoon style for children: " + prompt,
#             size="1024x1024",
#             quality="standard",
#             n=1
#         )
#         responses.append(response.data)
#     return responses

def create_image_from_story(client, image_prompts):
    return urls


test_summary = """
"prompt_1": "Dongle, a smooth, round egg with a cheerful smile, stands nervously in front of a wise, kind Black Hen in a cozy barn. The Hen looks thoughtful as she gives advice, with hay scattered around and sunlight streaming through the wooden beams.",
"prompt_2": "Dongle wrapped in a vibrant red calico cloth, sitting happily in a large copper kettle of boiling water, steam rising in a warm farmhouse kitchen. The Farmer’s Wife, wearing an apron, watches with a kind smile near a wooden hearth.",
"prompt_3": "Dongle emerges from the kettle, transformed with bright red spots across his smooth, shiny shell, looking vibrant and confident. The kitchen glows warmly, and the Farmer’s Wife claps her hands in delight as Humpty jumps with energy.",
"prompt_4": "Dongle, now dressed as a lively circus clown with colorful spots, performs tricks on a tightrope in a big-top tent. Children laugh and clap while he balances effortlessly, surrounded by bright lights and festive decorations.",
"prompt_5": "Dongle traveling through a lively landscape, carrying a banjo. He walks through a colorful countryside, waves to villagers, and spreads cheer under a bright blue sky with rolling hills in the distance."
"""


urls = [
    {'url': 'https://media.istockphoto.com/id/1885866215/photo/veterinarian-examines-the-pet.jpg?s=2048x2048&w=is&k=20&c=CuciaS7KvyEJOnCTIHIyuHd_oWdnBu4s8EdbybpKXGI='},
    {'url': 'https://media.istockphoto.com/id/2040984869/photo/big-eyed-naughty-cat-looking-at-the-target-from-behind-the-marble-table.jpg?s=2048x2048&w=is&k=20&c=e9NmDvB3arlyWmG4341yZWgZeYpiIuvxgDRNdgn4boQ='},
    {'url': 'https://media.istockphoto.com/id/2160576548/photo/veterinarian-examining-grey-cat-on-veterinary-table-in-clinic.jpg?s=2048x2048&w=is&k=20&c=h3nDa23j6Qhdd4hA1YjNX-LVzty-n8pq0G8NfrGgEjA='},
    {'url': 'https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg'},
    {'url': 'https://cdn.pixabay.com/photo/2015/11/16/14/43/cat-1045782_640.jpg'}
]
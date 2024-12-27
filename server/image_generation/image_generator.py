from openai import OpenAI
client = OpenAI()

def create_image_from_story(client, humpty_prompts):
    responses = []
    for prompt in humpty_prompts.values():  
        response = client.images.generate(
            model="dall-e-3",
            prompt="Make this image in cartoon style for children: " + prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        responses.append(response.data)
    return responses
    
humpty_prompts = {
    "prompt_1": (
        "Humpty Dumpty, a smooth, round egg with a cheerful smile, stands nervously in front of a wise, kind Black Hen "
        "in a cozy barn. The Hen looks thoughtful as she gives advice, with hay scattered around and sunlight streaming "
        "through the wooden beams."
    ),
    "prompt_2": (
        "Humpty Dumpty wrapped in a vibrant red calico cloth, sitting happily in a large copper kettle of boiling water, "
        "steam rising in a warm farmhouse kitchen. The Farmer’s Wife, wearing an apron, watches with a kind smile near a "
        "wooden hearth."
    ),
    "prompt_3": (
        "Humpty Dumpty emerges from the kettle, transformed with bright red spots across his smooth, shiny shell, looking "
        "vibrant and confident. The kitchen glows warmly, and the Farmer’s Wife claps her hands in delight as Humpty jumps "
        "with energy."
    ),
    "prompt_4": (
        "Humpty Dumpty, now dressed as a lively circus clown with colorful spots, performs tricks on a tightrope in a big-top "
        "tent. Children laugh and clap while he balances effortlessly, surrounded by bright lights and festive decorations."
    ),
    "prompt_5": (
        "Humpty Dumpty traveling through a lively landscape, carrying a banjo. He walks through a colorful countryside, waves "
        "to villagers, and spreads cheer under a bright blue sky with rolling hills in the distance."
    )
}

print(humpty_prompts)

image_url = create_image_from_story(client, humpty_prompts)

for i in image_url:
    print(i.url)
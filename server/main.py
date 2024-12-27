def turn_summary_into_image_prompts(test_summary):
    prompts_list = test_summary.strip().split('\n')
    image_prompts = [prompt.strip() for prompt in prompts_list]
    return image_prompts


def clean_prompts(image_prompts):
    # List comprehension to clean up the prompts
    cleaned_prompts = [item.split('": "', 1)[1].strip('",') for item in image_prompts]
    return cleaned_prompts


def merge_urls_with_prompts(prompts, urls):
    story = []
    for index, prompt in enumerate(prompts):
        try:
            story.append({'prompt': prompt, 'url': urls[index]['url']})
        except (IndexError, KeyError) as e:
            print(f"Error processing index {index}: {e}")
    return story

test_summary = """
"prompt_1": "Dongle, a smooth, round egg with a cheerful smile, stands nervously in front of a wise, kind Black Hen in a cozy barn. The Hen looks thoughtful as she gives advice, with hay scattered around and sunlight streaming through the wooden beams.",
"prompt_2": "Dongle wrapped in a vibrant red calico cloth, sitting happily in a large copper kettle of boiling water, steam rising in a warm farmhouse kitchen. The Farmer’s Wife, wearing an apron, watches with a kind smile near a wooden hearth.",
"prompt_3": "Dongle emerges from the kettle, transformed with bright red spots across his smooth, shiny shell, looking vibrant and confident. The kitchen glows warmly, and the Farmer’s Wife claps her hands in delight as Humpty jumps with energy.",
"prompt_4": "Dongle, now dressed as a lively circus clown with colorful spots, performs tricks on a tightrope in a big-top tent. Children laugh and clap while he balances effortlessly, surrounded by bright lights and festive decorations.",
"prompt_5": "Dongle traveling through a lively landscape, carrying a banjo. He walks through a colorful countryside, waves to villagers, and spreads cheer under a bright blue sky with rolling hills in the distance."
"""

urls = [
    {'url': 'http://example.com/image1.png'},
    {'url': 'http://example.com/image2.png'},
    {'url': 'http://example.com/image3.png'},
    {'url': 'http://example.com/image4.png'},
    {'url': 'http://example.com/image5.png'}
]

image_prompts = turn_summary_into_image_prompts(test_summary)
cleaned_prompts = clean_prompts(image_prompts)
story = merge_urls_with_prompts(cleaned_prompts, urls)

print(story)




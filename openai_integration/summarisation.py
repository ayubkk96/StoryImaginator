function_description = [
    {
        "name": "visualise_a_children_story",
        "description": "write a children's story with a plot, theme, characters"
    }
]


def abstract_summary_extraction(client, transcription):
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would "
                           "like you to read the following text and summarize it into a children's story to add comic style pictures to it"
                           "It needs to have a plot theme and characters."
                           "This summarisation needs to fit in Open AI's Dall-E-2 image generator prompt."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )

    return response.choices[0].message.content
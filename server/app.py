import glob
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from audio_processing.transcribe_audio import transcribe_audio
from audio_processing.trim_audio import refactor_audio
from openai_integration.openai_client import create_openai_client
from openai_integration.summarisation import (abstract_summary_extraction)
from server.image_generation.image_generator import create_image_from_story

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'mp4', 'm4a', 'avi'}  # Example allowed extensions
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB  # Example max file size (10 MB)


@app.route('/upload_audio', methods=['POST'])
def upload_audio_file():
    try:
        if 'audio_file' not in request.files:
            return jsonify({'error': 'No audio file part'}), 400

        audio_file = request.files['audio_file']
        print(audio_file.filename)
        if audio_file.filename == '':
            return jsonify({'error': 'No selected audio file'}), 400

        if audio_file.filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            return jsonify({'error': 'Invalid file format. Only audio and video files are allowed.'}), 400

        if audio_file.content_length > MAX_FILE_SIZE:
            return jsonify({'error': 'File size exceeds the maximum limit.'}), 400

        # Replace 'audio_uploads' with your desired directory for audio files
        audio_file.save('./' + audio_file.filename)
        # summary = summarise_audio(audio_file)

        print('Audio file saved successfully')

        image_prompts = turn_summary_into_image_prompts(test_summary)

        story = generate_images(image_prompts)


        if story is None:
            return jsonify({'error': 'An error occurred while turning the summary into a story'}), 500
        clear_directory('./Audio_files')
        return jsonify({'user_stories': story}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500   
    
def summarise_audio(audio_file):
    try:
        refactor_audio('./' + audio_file.filename, 'Audio_files')
        client = create_openai_client()
        transcription = transcribe_audio(client, './Audio_files')
        summary = abstract_summary_extraction(client, transcription)
        print(summary)
        return summary
    except Exception as e:
        return str(e)
    
def turn_summary_into_image_prompts(test_summary):
    print("Turning summary into image prompts")
    image_prompts = {}
    for i, prompt in enumerate(test_summary):
        image_prompts[f'prompt_{i+1}'] = prompt
    return image_prompts

def generate_images(image_prompts):
    try:
        client = create_openai_client()
        urls = create_image_from_story(client, image_prompts)
        story = merge_urls_with_prompts(image_prompts, urls)
        print(story)
        return story
    except Exception as e:
        return str(e)

def merge_urls_with_prompts(prompts, urls):
    story = []
    for i, prompt in prompts.items():
        story.append({'prompt': prompt, 'url': urls[i].url})
    return story

def clear_directory(directory_path):
    files = glob.glob(f'{directory_path}/*')
    for file in files:
        os.remove(file)

test_summary = """
"prompt_1": "Humpty Dumpty, a smooth, round egg with a cheerful smile, stands nervously in front of a wise, kind Black Hen in a cozy barn. The Hen looks thoughtful as she gives advice, with hay scattered around and sunlight streaming through the wooden beams.",
"prompt_2": "Humpty Dumpty wrapped in a vibrant red calico cloth, sitting happily in a large copper kettle of boiling water, steam rising in a warm farmhouse kitchen. The Farmer’s Wife, wearing an apron, watches with a kind smile near a wooden hearth.",
"prompt_3": "Humpty Dumpty emerges from the kettle, transformed with bright red spots across his smooth, shiny shell, looking vibrant and confident. The kitchen glows warmly, and the Farmer’s Wife claps her hands in delight as Humpty jumps with energy.",
"prompt_4": "Humpty Dumpty, now dressed as a lively circus clown with colorful spots, performs tricks on a tightrope in a big-top tent. Children laugh and clap while he balances effortlessly, surrounded by bright lights and festive decorations.",
"prompt_5": "Humpty Dumpty traveling through a lively landscape, carrying a banjo. He walks through a colorful countryside, waves to villagers, and spreads cheer under a bright blue sky with rolling hills in the distance."
"""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

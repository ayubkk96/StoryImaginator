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
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB
allowed_extensions = {'mp3', 'wav', 'mp4', 'avi'}


@app.route('/upload_audio', methods=['POST'])
def upload_audio_file():
    try:
        if 'audio_file' not in request.files:
            return jsonify({'error': 'No audio file part'}), 400

        audio_file = request.files['audio_file']
        print(audio_file.filename)
        if audio_file.filename == '':
            return jsonify({'error': 'No selected audio file'}), 400

        if audio_file.filename.split('.')[-1] not in allowed_extensions:
            return jsonify({'error': 'Invalid file format. Only audio and video files are allowed.'}), 400

        if audio_file.content_length > MAX_FILE_SIZE:
            return jsonify({'error': 'File size exceeds the maximum limit.'}), 400

        # Replace 'audio_uploads' with your desired directory for audio files
        audio_file.save('./' + audio_file.filename)
        summary = summarise_audio(audio_file)
        print('Audio file saved successfully')

        image_prompts = turn_summary_into_image_prompts(summary)

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

def turn_summary_into_image_prompts(summary):
    print("Turning summary into image prompts")


def turn_summary_into_story(summary):
    try:
        user_stories = []
        user_story = {}
        acceptance_criteria = []

        for line in summary.split("\n"):
            line = line.lstrip()  # Remove leading whitespace
            if line.startswith("id:"):
                if user_story:
                    user_story["acceptance_criteria"] = acceptance_criteria
                    user_stories.append(user_story)
                user_story = {"id": int(line.replace("id:", "").strip())}
                acceptance_criteria = []
            elif line.startswith("Title:"):
                user_story["title"] = line.replace("Title:", "").strip()
            elif line.startswith("Description:"):
                user_story["description"] = line.replace("Description:", "").strip()
            elif line.startswith("-"):
                acceptance_criteria.append(line.strip("- ").strip())

        if user_story:
            user_story["acceptance_criteria"] = acceptance_criteria
            user_stories.append(user_story)

        return user_stories

    except Exception as e:
        print(f"An error occurred in turn_summary_into_story: {e}")
        return None


def clear_directory(directory_path):
    files = glob.glob(f'{directory_path}/*')
    for file in files:
        os.remove(file)


prompts = {
    "prompt_1": "Humpty Dumpty, a smooth, round egg with a cheerful smile...",
    "prompt_2": "Humpty Dumpty wrapped in a vibrant red calico cloth...",
    "prompt_3": "Humpty Dumpty emerges from the kettle, transformed...",
    "prompt_4": "Humpty Dumpty, now dressed as a lively circus clown...",
    "prompt_5": "Humpty Dumpty traveling through a lively landscape..."
}

urls = [
    {'url': 'http://example.com/image1.png'},
    {'url': 'http://example.com/image2.png'},
    {'url': 'http://example.com/image3.png'},
    {'url': 'http://example.com/image4.png'},
    {'url': 'http://example.com/image5.png'}
]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

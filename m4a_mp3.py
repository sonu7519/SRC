from pydub import AudioSegment
from pydub.utils import which
import os

AudioSegment.converter = which("C:\\Users\\sonu.sharma.vn\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin")  # Update path if different


def convert_m4a_to_mp3(input_file, output_file=None):
    if output_file == None:
        output_file = os.path.splitext(input_file)[0] + ".mp3"

    # Convert and export
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="mp3")
    print(f"Converted: {input_file} → {output_file}")

# Example usage
convert_m4a_to_mp3("sql_injection.m4a")
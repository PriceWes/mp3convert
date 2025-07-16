from pydub import AudioSegment
import os

# Supported audio file extensions
SUPPORTED_FORMATS = (".m4a", ".aac", ".wav", ".flac", ".ogg", ".wma", ".mp4", ".aiff", ".webm")

def convert_to_mp3(input_path, output_path):
    file_ext = os.path.splitext(input_path)[1][1:].lower()
    
    try:
        audio = AudioSegment.from_file(input_path, format=file_ext)
    except Exception as e:
        print(f"❌ Error loading {input_path}: {e}")
        return

    try:
        audio.export(output_path, format="mp3", bitrate="192k")
        print(f"✅ Converted: {input_path} -> {output_path}")
    except Exception as e:
        print(f"❌ Error converting {input_path}: {e}")

def batch_convert_folder(folder_path, output_folder=None):
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):
                input_path = os.path.join(root, file)
                file_base = os.path.splitext(file)[0] + ".mp3"

                output_path = (
                    os.path.join(output_folder, file_base) if output_folder
                    else os.path.join(root, file_base)
                )

                # Skips if already converted
                if os.path.exists(output_path):
                    print(f"⏩ Skipping (already exists): {output_path}")
                    continue

                convert_to_mp3(input_path, output_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Batch convert audio files in a folder to MP3 (skips existing).")
    parser.add_argument("folder", help="Path to the folder with audio files")
    parser.add_argument("--output", help="Optional path to output folder for MP3s")
    args = parser.parse_args()

    batch_convert_folder(args.folder, args.output)

## Batch Audio Converter to MP3 OFFLINE

This Python script batch-converts supported audio files in a folder to MP3 format using [pydub](https://github.com/jiaaro/pydub). It skips files that have already been converted and optionally outputs them to a separate folder.

---

## ✨ Features

* Converts multiple audio formats to MP3 (`.m4a`, `.aac`, `.wav`, `.flac`, `.ogg`, `.wma`, `.mp4`, `.aiff`, `.webm`)
* Skips files already converted to MP3
* Supports custom output directory
* 192kbps MP3 quality

---

## ✅ Requirements

* Python 3.6+
* [pydub](https://github.com/jiaaro/pydub)
* [ffmpeg](https://ffmpeg.org/) (must be installed and added to your system PATH)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/mp3convert.git
cd mp3convert
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Linux/macOS
# OR
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install `ffmpeg` (required)

* **Ubuntu/Debian:**

  ```bash
  sudo apt-get install ffmpeg
  ```

* **macOS (with Homebrew):**

  ```bash
  brew install ffmpeg
  ```

* **Windows:**

  * Download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
  * Add `ffmpeg/bin` to your system PATH

---

## 🚀 Usage

```bash
python batch_convert_to_mp3.py <input_folder> [--output <output_folder>]
```

* `<input_folder>`: Directory containing audio files to convert
* `--output <output_folder>` *(optional)*: Destination directory for MP3 files. Defaults to input folder if not specified.

### 🔄 Example

Convert all audio files in `./music` and save MP3s to `./mp3s`:

```bash
python batch_convert_to_mp3.py ./music --output ./mp3s
```

---

## 📌 Notes

* Skips files that already exist in `.mp3` format in the output folder
* Only processes files with supported extensions
* Uses 192k bitrate for all MP3 conversions

---

## AUTHOR : PRICEWES



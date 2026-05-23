from utils.audio_precessor import (
    converting_to_wav,
    downloading_youtube_audio,
    audio_chunk,
)

def input_audio(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected YouTube URL. Downloading audio...")

        wav_path = downloading_youtube_audio(source)
    else:
         print("Detected local file. Converting to WAV...")
         wav_path = converting_to_wav(source)

    print("Chunking audio...")
    chunk = audio_chunk(wav_path)
    print(f"Audio ready — {len(chunk)} chunk(s) created.")
    return chunk
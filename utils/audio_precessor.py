import os
from pydub import AudioSegment
import yt_dlp


DOWNLOAD_DIR = "Downloades"
os.makedirs(DOWNLOAD_DIR, exist_ok = True)


def downloading_youtube_audio(url: str) ->str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info =  ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
        return filename
    


def converting_to_wav(input_path: str) -> str:
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")
    return output_path
    

def audio_chunk(input_wav: str, chunk_minutes: int = 10) -> list:
    audio = AudioSegment.from_wav(input_wav)
    chuck_ms = chunk_minutes * 60 * 1000

    chunks = []

    for i, start in enumerate(range(0, len(audio), chuck_ms)):
        chunk = audio[start: start + chuck_ms]
        chunk_path = f"{input_wav}_chunk_{i}.wav"
        chunk.export(chunk_path, format = "wav")

        chunks.append(chunk_path)

    return chunks

from utils.process_input import input_audio
from cores.transcriber import transcribe_chunk_whisper, transcribe_all


source = "https://youtu.be/g22nhtWhSQ0?si=DOvj-LjQWwivxJG1"

chunk = input_audio(source)

print(transcribe_all(chunk))
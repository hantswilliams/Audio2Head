import pandas 
import ffmpeg

fileLocation = '/Users/hantswilliams/Documents/development/python_projects/Audio2Head/demo/audio/rajivClassrecordingOriginal.m4a'
outputLocation = '/Users/hantswilliams/Documents/development/python_projects/Audio2Head/demo/audio/rajivClassrecordingOriginal.wav'

(
    ffmpeg
    .input(fileLocation)
    .output(outputLocation)
    .run()
)



ffmpeg.input(fileLocation)
ffmpeg.input(fileLocation)

stream = ffmpeg.input(fileLocation)
stream = ffmpeg.output(stream, outputLocation)
ffmpeg.run(stream)
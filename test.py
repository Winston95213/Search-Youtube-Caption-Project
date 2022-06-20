from pytube import YouTube
url = 'https://www.youtube.com/watch?v=-nXsfXtTacE&t=486s'
source = YouTube(url)
en_caption = source.captions['a.en']
en_caption_convert_to_srt = (en_caption.generate_srt_captions())
print(en_caption_convert_to_srt)
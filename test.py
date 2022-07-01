from pytube import YouTube
# url = 'https://www.youtube.com/watch?v=S32y9aYEzzo'
# source = YouTube(url)
# en_caption = source.captions['a.en']
# en_caption_convert_to_srt = (en_caption.generate_srt_captions())
# print(en_caption_convert_to_srt)

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
caption = yt.captions.get_by_language_code('en')
print(caption.generate_srt_captions())
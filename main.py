import music_tag
file = music_tag.load_file("06 - Outlaw Torn.mp3")
print(file['tracknumber'])
print(file['discnumber'])

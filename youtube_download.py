import pafy

url = str(input("Enter the url of the youtube video and get the audio of it downloaded!"))

video = pafy.new(url)

print('Title : {}'.format(video.title))
print('Rating : {}'.format(video.rating))
print('View Count : {}'.format(video.viewcount))
print('Author : {}'.format(video.author))

print('Length : {}'.format(video.duration))

audiostreams = video.audiostreams
audiostreams[3].download()

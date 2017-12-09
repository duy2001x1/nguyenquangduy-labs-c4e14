Use youtube-dl to:

from youtube_dl import YoutubeDL

1. Download video:
dl = YoutubeDL()
dl.download(['Link Youtube']) #download 1 video

dl = YoutubeDL()
dl.download(['Link Youtube 1', 'Link Youtube 2'], ['Link Youtube n']) #download n videos

2. Download audio:
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Link Youtube'])

3. Search and Download Video/Audio:
#Search and Download Video
options = {
    'default_search': 'ytsearch',
    'max_downloads' : 1
}
dl = YoutubeDL(options)
dl.download(['Your Searching Key Words'])

#Search and download Audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Your Searching Key Words'])

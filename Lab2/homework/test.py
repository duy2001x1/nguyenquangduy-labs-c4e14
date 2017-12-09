from youtube_dl import YoutubeDL

#Sample1:
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

#Sample2:
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=s9-exVFzz14','https://www.youtube.com/watch?v=XdBsAXOxYfo'])

#Sample3:
options = {
    'format' : 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=JZjRrg2rpic'])

#Sample4:
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])

#Sample5:
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Ta còn yêu nhau'])

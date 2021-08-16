# Why Newsboat?
Newsboat and MPV player is the best way to watch Youtube videos without ads, javascript and browser brakes.

# Why newsboat-youtube?
But the Youtube channel URL and Newsboat RSS URL have some differences in the format.

# newsboat-youtube
Add YouTube Channel to Newsboat URLs

# usage
```
for add channel:
newsboat_youtube_add.py -a https://www.youtube.com/channel/UCUZHFZ9jIKrLroW8LcyJEQQ
for delete channel:
newsboat_youtube_add.py -d https://www.youtube.com/channel/UCUZHFZ9jIKrLroW8LcyJEQQ
```

# result
```
[URL] https://www.youtube.com/feeds/videos.xml?channel_id=UCUZHFZ9jIKrLroW8LcyJEQQ
[Adding] https://www.youtube.com/feeds/videos.xml?channel_id=UCUZHFZ9jIKrLroW8LcyJEQQ to Newsboat list..
[Added] URL to Newsboat list. Now 69 URLs in file.
```

# if already exist
```
[URL] https://www.youtube.com/feeds/videos.xml?channel_id=UCUZHFZ9jIKrLroW8LcyJEQQ
YouTube Channel already exist in Newboat URLs. Nothing to do.
```

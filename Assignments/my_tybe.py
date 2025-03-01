import pytube
from pytube import YouTube
from pytube.innertube import InnerTube

# https://youtu.be/OvfK8BTiuC4?si=Mev4q36tHB9gt6SA

# https://youtu.be/-DXHnPAXlLY?si=chjKVdu9dzXP5x4Gs
yt = YouTube('https://www.youtube.com/watch?v=1kVK0MZlbI4')
# link = "https://youtu.be/OvfK8BTiuC4?si=Mev4q36tHB9gt6SA"
# # yt = YouTube(link)
# a = yt.title
# print("this is video title", a)
# print("this is video title", yt.thumbnail_url)
# print("this is video publish date", yt.publish_date)
# print("this is video publish date", yt.streaming_data)
# print("this is video publish date", yt.streams)

# ------------------------Testing Code------------------
url = "https://www.youtube.com/watch?v=1kVK0MZlbI4"
# print("this video link title Is::", video_title(url))
print(yt.thumbnail_url)
# -----------API issue so we can't get youtube video title see you later.
print(yt.title)
# print(yt.publish_date)
# print(yt.vid_info)
my_yt = InnerTube()
# this is same result of -> yt.vid_info
my_yt.player("1kVK0MZlbI4")
# print(my_yt.player("1kVK0MZlbI4"))
# print(my_yt.base_url)

# {'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8', 'contentCheckOk': True, 'racyCheckOk': True}
# print(my_yt.base_params)

# {'context': {'client': {'clientName': 'ANDROID_MUSIC', 'clientVersion': '5.16.51', 'androidSdkVersion': 30}}}
# print(my_yt.base_data)

# print(my_yt.base_url)  # https://www.youtube.com/youtubei/v1

# print(my_yt.player("1kVK0MZlbI4"))

# print(yt.check_availability())
print(pytube.__version__)

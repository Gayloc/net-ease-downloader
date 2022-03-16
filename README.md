# net-ease-downloader
网易云音乐下载器(无vip)

网课时期无聊弄出来的小玩意，主要是为了方便下载GTAV的电台歌曲，由于有歌曲信息获取的功能，大部分歌曲可以在游戏电台页面看到歌手和歌名就非常好。
整合歌词的功能没测试过，歌曲封面在手机上显示没问题，在Windows上时有时无的，不知道是不是Windows的锅。
因为我没有vip，所以也没有做vip解析的功能。
网易云api使用的是[Binaryify/NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi "网易云音乐 NodeJS 版 API")，部署到了vercel

##用法
直接运行程序，按照提示输入网易云歌曲id就可以自动下载
或者在终端运行，参数是网易云歌曲id
歌曲会下载到程序所在目录

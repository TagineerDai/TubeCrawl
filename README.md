# TubeCrawl
To crawl video of Ms1MCeleb from Youtube.

#### 2017-8-11
+ Crawl video with given keywords.

usage:  
```python single.py Andrew Ng```
  
1. Crawl [Youtube](https://youtube.com) by searching some keywords.  
2. Download the searched video.  
3. Save files as `/video/<name>/<name+index>.mp4`, to avoid name conflicting.  
4. Add request head to prevent banning.

#### TODO  
+ Add multi-thread mechanism.
+ Use ffmpeg to extract frames in a given sample ratio.
+ Use cv2 to finish the face detection and extraction. [Source code](https://github.com/JeeveshN/Face-Detect)
+ Crawl high resolution picture from google search.
+ **Match the high resolution face with those extracted from vedio frames.**
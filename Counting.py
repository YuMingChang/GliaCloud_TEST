import re

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

d_count = dict()
for url in urls:
    file = re.search(r'\w+\.\w+$', url).group()
    if d_count.get(file):
        d_count[file] += 1
    else:
        d_count[file] = 1

sorted_d_count = sorted(d_count.items(), key=lambda x:-x[1])
for i in sorted_d_count[:3]:
    print('{} {}'.format(i[0], i[1]))
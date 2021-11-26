import os

cnt = 0

for img_name in os.listdir("imgs"):

    name = ".".join(img_name.split(".")[:-1])
    template = """---
date: 8/10/2021 00:%s
title: %s
id: 42069069%s
image_name: %s
---""" % (
        str(cnt).zfill(2),
        name,
        str(cnt).zfill(3),
        img_name,
    )

    cnt += 1

    with open(os.path.join("contents", "home_" + name + ".md"), "w") as f:
        f.write(template)

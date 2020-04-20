def url2tag(file_id):
    img_url = url2imgurl(file_id)
    tag = f"<img src='{img_url}' alt='이미지!' width='300'>"
    return tag


def url2imgurl(file_id):
    url = "https://drive.google.com/a/student.snue.ac.kr/thumbnail?id={}"
    return url.format(file_id)

import random
with open("/home/vbommana/repos/non-work/typing-hound-of-baskerville/hound-of-baskerville.txt") as o:
    paragraphs = o.readlines()
    paragraphs = [item for item in paragraphs if len(item) > 250]
    print(random.choice(paragraphs))

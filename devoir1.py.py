i = 0
li = []
media = []
section = []
mots = []
page = []
while i < len(articles):
    li = articles[i].split(',')
    media.append(li[0])
    section.append(li[1])
    mots.append(li[2])
    page.append(li[3])
    i+=1

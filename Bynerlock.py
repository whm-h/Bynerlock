enfirst = 'a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZالفبپتثجچحخدذرزژسشصطظضعغفقکگلمنوهی1234567890!@#$%^&*()_+=-/\ .:;\"\'\t،,][}<>'
first = 'ৌৈাীূড়োে্িুچشسপরকতচыགནཔཚཛটংваьбюض7صཁསཧཨйфпоظ5طزཞཟའཕབসཙবرذлдমثقیযཀцукজཡར01енгшўзхམনفغعهবলལহཆཇཉཝاগদཤжэخحجячстبلངིེོུཅتཏཐདنمکدئوژ'
first1 = 'ৌৈাীূড়োে্িুچشسপরকতচыགནཔཚཛটংваьбюض7صཁསཧཨйфпоظ5طزཞཟའཕབসཙবرذлдমثقیযཀцукজཡར01енгшўзхམনفغعهবলལহཆཇཉཝاগদཤжэخحجячстبلངིེོུཅتཏཐདنمکدئوژ'
enfirst1 = 'a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZالفبپتثجچحخدذرزژسشصطظضعغفقکگلمنوهی1234567890!@#$%^&*()_+=-/\ .:;\"\'\t،,][}<>'
q = ''
#enlist = []
def fin(b):
    global q
    global enlist
    h = first.find(b)
    t = enfirst[h]
    q = q + t
    #enlist.append(t)


def unlocker(sttring):
    a = sttring
    lenn = len(a)

    lem = 0
    while lem < lenn:
        b = a[lem]
        fin(b)
        lem = lem + 1
    encode = q

    print(encode)

def fin1(b):
    global q
    global enlist1
    h = enfirst1.find(b)
    t = first1[h]
    q = q + t
    #enlist.append(t)


def locking(sttring):
    global q
    q = ''

    lenn = len(sttring)
    print(type(lenn))

    lem = 0
    while lem < lenn:
        b = sttring[lem]
        fin1(b)
        lem = lem + 1
    encode = q

    print(encode)

import re
import urllib.request
import pprint
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import defaultdict

frequency = {}


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

# articles
bus = urllib.request.urlopen('https://www.tripadvisor.com.my/ShowUserReviews-g298570-d6652603-r527465461'
                             '-GO_KL_City_Bus-Kuala_Lumpur_Wilayah_Persekutuan.html').read()
# print(text_from_html(bus))
print('Article 1 extracted...')
train = urllib.request.urlopen('https://en.antaranews.com/news/122433/using-mrt-to-go-around-kuala-lumpur').read()
# print(text_from_html(mrt))
print('Article 2 extracted...')
walk = urllib.request.urlopen('https://www.marketing-interactive.com/tourism-malaysia-and-barbie-get-malaysians'
                              '-walking-around-town-with-their-dolls').read()
# print(text_from_html(walk))
print('Article 3 extracted...')
car = urllib.request.urlopen('https://www.entrepreneur.com/article/334690').read()
# print(text_from_html(car))
print('Article 4 extracted...')

res1 = len(bus.split())
res2 = len(train.split())
res3 = len(walk.split())
res4 = len(car.split())

print('Total number of words for the first article: \n', (res1), 'words')
print('Total number of words for the second article: \n', (res2), 'words')
print('Total number of words for the third article: \n', (res3), 'words')
print('Total number of words for the fourth article: \n', (res4), 'words')

print('           Word Frequency for the 1st article: ')
print('▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼')
# ni method utk cari all the word frequency dalam web html tu
one_text = (text_from_html(bus)).lower()
one_pattern = re.findall(r'\b[a-z]{3,15}\b', one_text)

for word in one_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
    semua = frequency[word]+count

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])


print('           Word Frequency for the 2nd article: ')
print('▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼')
two_text = (text_from_html(train)).lower()
two_pattern = re.findall(r'\b[a-z]{3,15}\b', two_text)
for word in two_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])

print('           Word Frequency for the 3rd article: ')
print('▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼')
three_text = (text_from_html(walk)).lower()
three_pattern = re.findall(r'\b[a-z]{3,15}\b', three_text)
for word in three_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])

print('           Word Frequency for the 4th article: ')
print('▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼')
four_text = (text_from_html(car)).lower()
four_pattern = re.findall(r'\b[a-z]{3,15}\b', four_text)

for word in four_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])

print('           Stop Words Frequency: ')
print('▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━▼')


def search(word, text):  # using rabin-karp algorithm method untuk cari stop words and frequency dia
    m = len(word)
    n = len(text)

    counter = 0

    for i in range(0, n - m + 1):
        found = True
        for j in range(0, m):
            if word[j] != text[i + j]:
                found = False
                break
        if found:
            counter += 1

    if counter == 0:
        print('The word', word, 'has no match')
    else:
        if counter > 1:
            print('The word', word, 'appears: ', counter, 'times!')
        if counter == 1:
            print('The word', word, 'appears: ', counter, 'time!')


collection_a = [one_text, two_text, three_text, four_text]
pat = 'i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself ' \
      'it its itself they them their theirs themselves what which who whom this that these those am is are was were be ' \
      'been being have has had having do does did doing a an the and but if or because as until while of at by for ' \
      'with about against between into through during before after above below to from up down in out on off over ' \
      'under again further then once here there when where why how all any both each few more most other some such no ' \
      'nor not only own same so than too very s t can will just don should now '
# pat ni list of stopwords
for x in collection_a:
    for stop_words in pat.split():
        search(stop_words, x)

# ni utk delete stopwords
for x in collection_a:
    resultwords = [word for word in re.split("\W+", x) if word.lower() not in stop_words]
    print('━━━━━━━━━━━━━━━━ ✠ ━━━━━━━━━━━━━━━━')
    print('          Without stopwords: ')
    print('━━━━━━━━━━━━━━━━ ✠ ━━━━━━━━━━━━━━━━')
    print()
    if x == collection_a[0]:
        result1 = ' '.join(resultwords)
        len1 = len(result1.split())
        print('Stop words frequency for article 1:', (len1))
    if x == collection_a[1]:
        result1 = ' '.join(resultwords)
        len2 = len(result1.split())
        print('Stop words frequency for article 2:', (len2))
    if x == collection_a[2]:
        result1 = ' '.join(resultwords)
        len3 = len(result1.split())
        print('Stop words frequency for article 3:', (len3))
    if x == collection_a[3]:
        result1 = ' '.join(resultwords)
        len4 = len(result1.split())
        print('Stop words frequency for article 4:', (len4))


# positive words file
f = open('positive_words.txt')
positive = f.read()
f.close()
# negative words file
f = open('negative_words.txt')
negative = f.read()
f.close()


def boyer_moore_horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    found_indexes = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)

        k += skip[ord(text[k])]

    return found_indexes


print()
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('         Positive & Negative words: ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

tvebus = 0
tvewalk = 0
tvetrain = 0
tvecar = 0
nvebus = 0
nvewalk = 0
nvetrain = 0
nvecar = 0

for x in collection_a:
    for pos_words in positive.split():
        boyer_moore_horspool(pos_words, x)
        if x == collection_a[0]:
            if pos_words in x:
                tvebus += 1
        elif x == collection_a[1]:
            if pos_words in x:
                tvetrain += 1
        elif x == collection_a[2]:
            if pos_words in x:
                tvewalk += 1
        elif x == collection_a[3]:
            if pos_words in x:
                tvecar += 1

# print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
# print('            Negative words: ')
# print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
for x in collection_a:
    for neg_words in negative.split():
        boyer_moore_horspool(neg_words, x)
        if x == collection_a[0]:
            if neg_words in x:
                nvebus += 1
        elif x == collection_a[1]:
            if neg_words in x:
                nvetrain += 1
        elif x == collection_a[2]:
            if neg_words in x:
                nvewalk += 1
        elif x == collection_a[3]:
            if neg_words in x:
                nvecar += 1

print()
print('Total positive words for article one is', tvebus)
print('Total positive words for article two is', tvetrain)
print('Total positive words for article three is', tvewalk)
print('Total positive words for article four is', tvecar)
print()
print('Total negative words for article one is', nvewalk)
print('Total negative words for article two is', nvetrain)
print('Total negative words for article three is', nvewalk)
print('Total negative words for article four is', nvecar)

print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('            Conclusion: ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

ListA = [tvebus, tvetrain, tvewalk, tvecar]
ListB = [nvebus, nvetrain, nvewalk, nvecar]

for x in ListA:
    if x == ListA[0]:
        if x > ListB[0]:
            print('The article with regards to using bus as public transport is giving positive sentiment')
        else:
            print('The article with regards to using bus as public transport is giving negative sentiment')
    if x == ListA[1]:
        if x > ListB[1]:
            print('The article with regards to using train as public transport is giving positive sentiment')
        else:
            print('The article with regards to using train as public transport is giving negative sentiment')
    if x == ListA[2]:
        if x > ListB[2]:
            print('The article with regards to using walk as public transport is giving positive sentiment')
        else:
            print('The article with regards to using walk as public transport is giving negative sentiment')
    if x == ListA[3]:
        if x > ListB[3]:
            print('The article with regards to using car as public transport is giving positive sentiment')
        else:
            print('The article with regards to using car as public transport is giving negative sentiment')

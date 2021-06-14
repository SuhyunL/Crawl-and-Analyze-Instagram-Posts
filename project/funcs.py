from instalooter.looters import HashtagLooter
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
dler._status_cache['panlex_lite'] = 'installed' # Trick the index to treat panlex_lite as it's already installed.
dler.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import re
import os


def hashtagSearch(keyword, number):
    looter = HashtagLooter(f'{keyword}')
    _baseurl = "https://www.instagram.com/p"
    i = 0
    results = []
    looter.login('onlyforcrawl', 'dlttngus23//')
    for media in looter.medias():
        i += 1
        try:
                text = media['edge_media_to_caption']['edges'][0]['node']['text']
        except Exception:
                continue
        except IndexError:
                i -=1
                pass
        result = {
                'hashtag' : keyword,  ##찾을 수 있도록 수정
                'writer' : int(media['owner']['id']),
                'caption' : text,
                'tags' : re.findall(r"#(\w+)", text),
                'img_url' : media['thumbnail_src']
        }
        result['caption'] = re.sub('[^a-zA-Z]', ' ', result['caption']) ##caption datatype 문자에 맞도록
        if 'sportyandrichthailand' in result['tags']:
          pass
        else:
          results.append(result)

        if i == number:
            return results
            break


def parsingWords(results, type, keyword):
    parsed_words = []
    for r in results:
      if type == 'caption':
        targets = word_tokenize(r['caption'])
        if 'Line' in targets:
          targets = []
      if type == 'tags':
        targets = r['tags']
      for t in targets:
        try:
          p = re.search(r'[\w]+', t).group(0)
          if p in ['and','in','to','the', 'I', 'me','her','him','her','we','our','their','those','all','be','with','of','you','a','size','ม','my','is','am','are','Size','Price','เป','it','this','that','of','1','2','3','4','5','6','for','to','ส']:
            pass
          elif p != keyword :
            parsed_words.append(p)
        except AttributeError : continue
    return parsed_words


def commonWord(list, number):
    result = FreqDist(list)
    return result.most_common(number) #returns in tuples-in-list

import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.express as px
def plotlygraph(x_list, y_list):
    plot = px.scatter(
      x = x_list, y = y_list, title = 'Analysis Result', size=y_list, size_max=90
    )
    html = plot.write_html('/Users/isuhyun/Desktop/sp3_project/project/templates/analysis.html',
                full_html=True,
                include_plotlyjs='cdn')

    return html
  # import plotly.graph_objects as go
  # size = y_list
  # fig = go.Figure(data=[go.Scatter(
  #     x=x_list, y=y_list,
  #     mode='markers',
  #     marker=dict(
  #         size=size,
  #         sizeref=2.*max(size)/(15.**2)
  #     )
  # )])
  # plot_file = fig.to_json()
  # return plot_file

#print(hashtagSearch('jacquemus', 100))
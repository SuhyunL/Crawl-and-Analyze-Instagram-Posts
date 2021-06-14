from flask import Blueprint, render_template, request, redirect, url_for
from project.funcs import hashtagSearch, parsingWords, commonWord, plotlygraph
from project.models import db, Crawler
from bokeh.plotting import figure, output_file, show

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/keyword')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=["GET", "POST"])
def analyze():   
    if request.method == "POST":
        keyword = request.form['hashtags']#form 메서드로 받아오기
        if keyword == '#':
            print('no keyword')
            return redirect(url_for('main.index'))

        keyword = keyword.split('#')[1]
        # original_data = Crawler.query.filter_by(hashtag = keyword).first()
        # if original_data is not None:
        #     datas = Crawler.query.filter_by(hashtag = keyword).all()
        #     db.session.delete(datas)
        hashes = hashtagSearch(keyword, 2000)
        print('---------------------------',len(hashes))

        for has in hashes:
            try:
                db.session.add(Crawler(hashtag = has['hashtag'], img_url = has['img_url']))
                db.session.commit()
            except Exception:
                pass

        parsed_captions = parsingWords(hashes, type = 'caption', keyword=keyword)
        parsed_tags = parsingWords(hashes, type = 'tags', keyword=keyword)
        result_c = commonWord(parsed_captions, 500)
        result_t = commonWord(parsed_tags, 500)

        result_c_index = list(map(lambda x: x[0], result_c))
        result_c_value = list(map(lambda x: x[1], result_c))
        result_t_index = list(map(lambda x: x[0], result_t))
        result_t_value = list(map(lambda x: x[1], result_t))
        
        plotlygraph(result_c_index, result_c_value)
        #plotlygraph(result_t_index, result_t_value)
        
        return render_template('analysis.html') #render_template('analysis.html', graph_1 = graph_1, graph_2 = graph_2)
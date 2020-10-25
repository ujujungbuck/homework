# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://platum.kr/archives/120958'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# og_image = soup.select_one('meta[property="og:image"]')
# og_title = soup.select_one('meta[property="og:title"]')
# og_description = soup.select_one('meta[property="og:description"]')
#
# url_title = og_title['content']
# url_description = og_description['content']
# url_image = og_image['content']
#
# article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
#            'comment': comment_receive}
#
# # 3. mongoDB에 데이터를 넣기
# db.articles.insert_one(article)
#
# return jsonify({'result': 'success'})
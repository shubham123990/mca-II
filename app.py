import email
from flask import Flask,render_template,request,redirect
from newsapi import NewsApiClient

from ModulePackage.user import user

app= Flask(__name__)

@app.route("/",methods=['POST','GET'])
def login():
    
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        validstatus = user.checkvaliduser(email,password)
        if validstatus:
            return redirect('/home')
        else:
            return render_template('login.html')


    return render_template('login.html')


@app.route("/signup" ,methods=['POST','GET'])
def signup():

    if request.method =='POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        bdate = request.form.get('bdate')
        password = request.form.get('password')

        user(fname,lname,email,bdate,password)

        '''validstatus =user.checkemail(email)
        if validstatus:
            print("registration succesfull")
        else:
            print("email already register")'''

    return render_template('signup.html')

   




@app.route("/home")
def home():
    api_key = '25560f3cf53c433c9807c60595b373a6'
    
    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(sources = "bbc-news")
    all_articles = newsapi.get_everything(sources = "bbc-news")

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []   
    url_all = []

    for j in range(len(a_articles)): 
        main_all_articles = a_articles[j]   

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
        
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('home.html',contents=contents,all = all)




    


    






if __name__ == '__main__':
    app.run(debug=True)



const http = require('superagent'),
config = require('../config');


module.exports = {

getNewsHeadlines: (source = 'techcrunch')=>{
    http.get(`https://newsapi.org/v1/articles`
    ).query({ apiKey: config.newsApiKey, source: source})
    .end((err, res)=>{
        const resObj = JSON.parse(res.text)
        const articles = resObj.articles;
        articles.forEach((article)=>{
            console.log(article.title)
        })
    })
}



}

const http = require('superagent'),
config = require('../config');
var exec = require('child_process').exec;


module.exports = {
    getNewsHeadlines: (source = 'techcrunch')=>{
        http.get(`https://newsapi.org/v1/articles`
        ).query({ apiKey: config.newsApiKey, source: source})
        .end((err, res)=>{
            const resObj = JSON.parse(res.text)
            const articles = resObj.articles;
            var headlines = "";
            articles.forEach((article)=>{
                headlines+= article.title + '    ';
            })

            var cmd = `sudo ./runtext.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE -c 2 -t '${headlines}'`;
            exec(cmd, {cwd:'/home/pi/led/utils/matrix/python/samples'}, function(error, stdout, stderr) {
                if (error) {
                  console.error(`exec error: ${error}`);
                  return;
                }
                console.log(`stdout: ${stdout}`);
                console.log(`stderr: ${stderr}`);
            });

        })
    }
}

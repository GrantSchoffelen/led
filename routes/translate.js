var express = require('express');
var router = express.Router();
const translate = require('google-translate-api');
const config = require('../config');
const client = require('twilio')(config.accountSid, config.authToken);
const MessagingResponse = require('twilio').twiml.MessagingResponse;
var exec = require('child_process').exec;





router.post('/', (req, res, next) => {
    translate(req.body.Body, {from: 'en', to: 'fr'}).then(response => {
        client.messages.create({
            to: '+16094396656',
            from: '+16096143551',
            body: response.text
        }).then((message) => {
            var cmd = `sudo ./runtext.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE -c 2 -t "${response.text}"`;
            exec(cmd, {cwd: config.pathToMatrixLib+'/python/samples'}, function(error, stdout, stderr) {
                if (error) {
                  console.error(`exec error: ${error}`);
                  return;
                }
                console.log(`stdout: ${stdout}`);
                console.log(`stderr: ${stderr}`);
            });
        });
    }).catch(err => {
        console.error(err);
    });
});

module.exports = router;

var exec = require('child_process').exec;
var config = require('../config');

module.exports = {
    startTemp: function(){
        var cmd = `sudo ./temp.py -c 2`;
        exec(cmd, {cwd: config.pathToMatrixLib + '/python/samples'}, function(error, stdout, stderr) {
            if (error) {
              console.error(`exec error: ${error}`);
              return;
            }
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        });
    }
}

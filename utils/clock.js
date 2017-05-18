var exec = require('child_process').exec;
var config = require('../config');

module.exports = {
    startClock: function(){
        var cmd = `sudo ./time.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE -c 2`;
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

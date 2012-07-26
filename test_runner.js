
var spawn, input, child, buffer;

spawn = require('child_process').spawn;

input = {
  name: "top_k",
  argv: [ 10 ],
  kwargs: { c: 5 }
};

child = spawn('python', ['test_external.py']);
child.stdin.write( JSON.stringify(input) );
child.stdin.end();
buffer = '';
child.stdout.on('data', function (data) {
  buffer += data.toString();
});
child.stderr.on('data', function (data) {
  buffer += data.toString();
});
child.on('exit', function (code, signal) {
  try {
    var output = JSON.parse(buffer);
    console.log('out:', output);
  } catch (err) {
    console.log('error:', buffer);
    console.log('code:', code, 'signal:', signal);
  }
});

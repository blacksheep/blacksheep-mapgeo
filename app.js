var express = require('express')
var serveStatic = require('serve-static')

var app = express()
var bodyParser = require('body-parser');

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(serveStatic(__dirname+'/static/', {'index': ['index.html', 'index.htm']}));

var port = process.env.PORT || 3000;

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router
var ips = {};

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    var count;
    if (ips[ip]) {
      count = ips[ip];
      count--;
      ips[ip] = count;
    } else if( ips[ip] <= 0 ){
      res.status = 400;
      res.end('something went wrong...');
      return;
    } else {
      ips[ip] = count = 3;
    }

    console.log('IP: '+ip + ' Count: '+ count);

    if(count){
      next(); // make sure we go to the next routes and don't stop here
    } else {
      var message = 'IP: '+ip + ' You have used up all your count: '+ count;
      res.json({ message: message });
      // request.pause();
    }
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });
});


var Location = require('./models/Location');

router.route('/location')
    .get(function(req, res) {
    // .post(function(req, res) {

        var location = new Location();
        location.city = req.body.city;
        console.log(JSON.stringify(location));
        console.log("LOOK UP LOCATION");
        console.log(req.query);

        res.json({ message: 'lookup location created!' });
        // save the bear and check for errors
        // bear.save(function(err) {
        //     if (err)
        //         res.send(err);
        //
        //     res.json({ message: 'Bear created!' });
        // });

    });



app.use('/api/free', router);

app.listen(port);
console.log('Listening on http://localhost:' + port);

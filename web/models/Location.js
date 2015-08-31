var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var LocationSchema   = new Schema({
    city: String,
    zipCode: Number,
    latitude: String,
    longitude: String
});

module.exports = mongoose.model('Location', LocationSchema);

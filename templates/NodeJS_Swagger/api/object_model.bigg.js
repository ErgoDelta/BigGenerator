/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/*
  DOC COMMENTS GO HERE
*/

var mongoose = require('mongoose'),
Schema = mongoose.Schema;

var ModelSchema = new Schema({
  name: String,
  info: String,
  active: Boolean,
  world: Schema.Types.Mixed
});

module.exports = mongoose.model('${model["name"]}', ModelSchema);

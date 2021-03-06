/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/*
  DOC COMMENTS GO HERE
*/

var ${model["name"]} = require('./${model["name"]}.model');

exports.register = function(socket) {
  ${model["name"]}.schema.post('save', function (doc) {
    onSave(socket, doc);
  });
  ${model["name"]}.schema.post('remove', function (doc) {
    onRemove(socket, doc);
  });
}

function onSave(socket, doc, cb) {
  socket.emit('${model["name"]}:save', doc);
}

function onRemove(socket, doc, cb) {
  socket.emit('${model["name"]}:remove', doc);
}

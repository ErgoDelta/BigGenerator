/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/**
* Using Rails-like standard naming convention for endpoints.
* GET     /game              ->  index
* POST    /game              ->  create
* GET     /game/:id          ->  show
* PUT     /game/:id          ->  update
* DELETE  /game/:id          ->  destroy
*/

/*
  DOC COMMENTS GO HERE
*/

var _ = require('lodash');
var Model = require('./${model["name"]}.model');

// Get list of ${model["name"]}s
exports.index = function(req, res) {
  Model.find(function (err, ${model["name"]}s) {
    if(err) { return handleError(res, err); }
      return res.json(200, ${model["name"]}s);
    });
  };

// Get a single ${model["name"]}
exports.show = function(req, res) {
  Model.findById(req.params.id, function (err, ${model["name"]}) {
    if(err) { return handleError(res, err); }
      if(!game) { return res.send(404); }
        return res.json(${model["name"]});
      });
    };

// Creates a new ${model["name"]} in the DB.
exports.create = function(req, res) {
  Model.create(req.body, function(err, ${model["name"]}) {
    if(err) { return handleError(res, err); }
      return res.json(201, ${model["name"]});
    });
  };

// Updates an existing game in the DB.
exports.update = function(req, res) {
  if(req.body._id) { delete req.body._id; }
    Model.findById(req.params.id, function (err, ${model["name"]}) {
      if (err) { return handleError(res, err); }
        if(!${model["name"]}) { return res.send(404); }
          var updated = _.merge(${model["name"]}, req.body);
          updated.save(function (err) {
            if (err) { return handleError(res, err); }
              return res.json(200, ${model["name"]});
            });
          });
        };

// Deletes a game from the DB.
exports.destroy = function(req, res) {
  Model.findById(req.params.id, function (err, ${model["name"]}) {
    if(err) { return handleError(res, err); }
    if(!${model["name"]}) { return res.send(404); }
    ${model["name"]}.remove(function(err) {
      if(err) { return handleError(res, err); }
        return res.send(204);
      });
    });
  };

function handleError(res, err) {
  return res.send(500, err);
}

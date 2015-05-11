/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/**
 * Populate DB with sample data on server start
 * to disable, edit config/environment/index.js, and set `seedDB: false`
 */

/*
  DOC COMMENTS GO HERE
*/

var ${model["name"]} = require('../api/${model["name"]}/${model["name"]}.model');

${model["name"]}.
  find({}).
  remove(function() {
    User.create({
        TODO : 'Need to fill out expected fields and data'
      },
      function() {
        console.log('finished populating ${model["name"]}');
      }
    );
  });

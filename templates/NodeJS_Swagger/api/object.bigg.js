/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/*
  DOC COMMENTS GO HERE
*/

var express = require('express');
var controller = require('./${model["name"]}.controller');
var config = require('../../config/environment');
var auth = require('../../auth/auth.service');

var router = express.Router();

//
router.post('/', auth.hasRole('admin'), controller.create);
router.delete('/:id', auth.hasRole('admin'), controller.destroy);

//
router.get('/', auth.isAuthenticated(), controller.index);
router.get('/:id', auth.isAuthenticated(), controller.show);
router.put('/:id', auth.isAuthenticated(), controller.update);


module.exports = router;

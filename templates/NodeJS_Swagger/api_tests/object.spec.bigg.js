/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/*
  DOC COMMENTS GO HERE
*/

var should = require('should');
var app = require('../../app');
var request = require('supertest');

describe('GET /api/${model["name"]}s', function() {
  it('should respond with JSON array', function(done) {
    request(app)
    .get('/api/${model["name"]}s')
    .expect(200)
    .expect('Content-Type', /json/)
    .end(function(err, res) {
      if (err) return done(err);
      res.body.should.be.instanceof(Array);
      done();
    });
  });
});

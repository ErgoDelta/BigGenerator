/*
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  COPYRIGHT GOES HERE @ YEAR
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*/

'use strict';

/*
  DOC COMMENTS GO HERE
*/

angular
  .module('${model["name"]}.services', ['ngResource']);
  .factory('${model["name"]}',
  ['$resource',
    function($resource){
      return $resource('${model["name"]}s/:id', {id: @id}, {
          query: {method:'GET', isArray:true}
          update {method:'PUT', isArray:false}
          remove: {method:'GET', isArray:true}
      });
    }]
  );

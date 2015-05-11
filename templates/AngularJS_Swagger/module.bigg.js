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
  .module('${module}')
  .config(['$stateProvider',
    function ($stateProvider) {
      $stateProvider
        .state('${model["name"]}.create', {
          url: '/${model["name"]}/create',
          templateUrl: 'app/${module}/${model["name"]}-create.html',
          controller: '${model["name"]}.create.ctrl'
        })
        .state('${model["name"]}.update', {
          url: '/${model["name"]}/update',
          templateUrl: 'app/${module}/${model["name"]}-update.html',
          controller: '${model["name"]}.update.ctrl'
        })
        .state('gameDelete', {
          url: '/${model["name"]}/:id/delete',
          templateUrl: 'app/${module}/${model["name"]}-delete.html',
          controller: '${model["name"]}.delete.ctrl',
          authenticate: true
        })
        .state('gameView', {
          url: '/${model["name"]}/:id/details',
          templateUrl: 'app/${module}/${model["name"]}-details.html',
          controller: '${model["name"]}.details.ctrl'
        })
        .state('gameMove', {
          url: '/${model["name"]}/:id/list',
          templateUrl: 'app/${module}/${model["name"]}-list.html',
          controller: '${model["name"]}.list.ctrl'
        });
    }]
  );

'use strict'
var app = angular.module('chirper-app', ['chirper.api'])

app.config(function($httpProvider) {
    $httpProvider.defaults.headers.post  = {
        'X-CSRFToken': $.cookie('csrftoken'),
        'Content-Type': 'application/json'
    };
});


app.directive('hideIfLoginRequired', function() {
  return {
    restrict: 'A',
    link: function($scope,elem,attrs) {

       elem.hide();

      $scope.$on('auth-loginRequired', function() {
        elem.hide();
      });

      $scope.$on('auth-loginConfirmed', function() {
        elem.show();
      });

    }
  }
});

app.directive('showIfLoginRequired', function() {
  return {
    restrict: 'A',
    link: function($scope,elem,attrs) {

      elem.hide();

      $scope.$on('auth-loginRequired', function() {
        elem.show();
      });

      $scope.$on('auth-loginConfirmed', function() {
        elem.hide();
      });

    }
  }
});
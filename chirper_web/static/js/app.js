'use strict'
var app = angular.module('chirper-app', ['chirper.api'])

app.config(function($httpProvider) {
    $httpProvider.defaults.headers.post  = {
        'X-CSRFToken': $.cookie('csrftoken'),
        'Content-Type': 'application/json'
    };
});


app.directive('hideIfLoginRequired', ['AuthService', function(AuthService) {
  return {
    restrict: 'A',
    link: function($scope,elem,attrs) {
      
      if(AuthService.isLoggedIn()){
        elem.show();
      }
      else {
        elem.hide();
      }

      $scope.$on('auth-loginRequired', function() {
        elem.hide();
      });

      $scope.$on('auth-loginConfirmed', function() {
        elem.show();
      });

    }
  }
}]);

app.directive('showIfLoginRequired', ['AuthService', function(AuthService) {
  return {
    restrict: 'A',
    link: function($scope,elem,attrs) {

      if(AuthService.isLoggedIn()){
        elem.hide();
      }
      else {
        elem.show();
      }

      $scope.$on('auth-loginRequired', function() {
        elem.show();
      });

      $scope.$on('auth-loginConfirmed', function() {
        elem.hide();
      });

    }
  }
}]);
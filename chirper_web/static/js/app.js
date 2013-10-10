'use strict'

angular.module('chirper', ['chirper.api']).config(function($httpProvider) {
    $httpProvider.defaults.headers.post  = {
        'X-CSRFToken': $.cookie('csrftoken'),
        'Content-Type': 'application/json'
    };
});
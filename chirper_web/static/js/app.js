'use strict'

angular.module('chirper', ['chirpTimelineService']).config(function($httpProvider) {
    $httpProvider.defaults.headers.post  = {
        'X-CSRFToken': $.cookie('csrftoken'),
        'Content-Type': 'application/json'
    };
});
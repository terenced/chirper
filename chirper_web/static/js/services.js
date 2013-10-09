angular.module('chirpTimelineService', ['ngResource']).
    factory('ChirpTimeline', function($resource){
        return $resource('/api/chirps/timeline', {}, {
            query: {method:'GET', isArray:true}
  });

});
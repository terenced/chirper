app = angular.module('chirper.api',['ngResource'])

app.factory('ChirpsService', function($resource){
        return $resource('/api/chirps', {}, {
            query: {method:'GET', isArray:true},
            save: {method:'POST', isArray:false}
        });
    });


app.factory('UsersService', function($resource){
        return $resource('/api/users', {}, {
            query: {method:'GET', isArray:true}
        });
    });
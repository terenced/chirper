var app = angular.module('chirper.api', ['ngCookies', 'ngResource'])

app.factory('ChirpsService', function($http,$q, $cookieStore){
        return {
            getChirps: function() {
                var deferred = $q.defer();
                console.log('requesting with ' + $cookieStore.get('user').username + ' ' + $cookieStore.get('user').token)
                $http.defaults.headers.get = { 'Authorization': 'Token ' + $cookieStore.get('user').token }
                 var promise = $http.get('/api/chirps').success(function(response){
                    deferred.resolve(response);
                });
                return deferred.promise; 
            },

            create: function(chirp){
                data = {'chirp': chirp}
                $http.defaults.headers.post = { 'Authorization': 'Token ' + $cookieStore.get('user').token, 'Content-Type': 'application/json'  }
                return $http.post('/api/chirps/create', data)
            }
        }
});

app.factory('UsersService', function($resource){
        return $resource('/api/users', {}, {
            query: {method:'GET', isArray:true}
        });
});

app.factory('AuthService', function($http, $cookieStore) {

    var noUser = { username: '', token: '' }
    var currentUser = null//$cookieStore.get('user') || noUser

    function changeUser(u, t) {
        console.log('changeUser')
        console.log(u + ":" + t)
        clearUser();
        currentUser = { username: u, token: t };
        $cookieStore.put('user', currentUser);
    };

    function clearUser(){
        console.log('cookieStore ' + $cookieStore)
        $cookieStore.remove('user');
        currentUser = noUser;
    }


    return {
        load: function(){
            currentUser = $cookieStore.get('user') || noUser
        },

        isLoggedIn: function() {
            return currentUser.token != ''
        },

        register: function(user, success, error) {
            $http.post('/api/register', user).success(function(res) {
                changeUser(user.username, res.token);
                success();
            }).error(error);
        },
        login: function(user, success, error) {
            $http.post('/api/token-auth', user).success(function(res){
                changeUser(user.username, res.token);
                success({ username: user.username, token: res.token });
            }).error(error);
        },
        logout: function(callback) {
            clearUser();
            callback();
        },

        getUser: function() {
            return currentUser;
        }
    };
});
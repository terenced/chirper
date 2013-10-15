var app = angular.module('chirper.api', ['ngCookies', 'ngResource'])

// app.factory('ChirpsService', function($resource, $cookieStore){
//         return $resource('/api/chirps', {}, {
//             query: {
//                 method:'GET',
//                 isArray:true,
//                 headers:{ 'Authorization': 'Token ' + $cookieStore.get('user').token }
//             },
//             save: {method:'POST', isArray:false}
//         });
//     });

app.factory('ChirpsService', function($http,$q, $cookieStore){
        return {
            getChirps: function() {
                var deferred = $q.defer();
                $http.defaults.headers.get = { 'Authorization': 'Token ' + $cookieStore.get('user').token }
                 var promise = $http.get('/api/chirps').success(function(response){
                    deferred.resolve(response);
                });
                return deferred.promise; 
            },

            create: function(chirp){
                data = {'chirp': chirp}
                console.log(data)
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

    var currentUser = $cookieStore.get('user') || { username: '', token: '' };

    function changeUser(u, t) {
        $cookieStore.remove('user');
        currentUser = { username: u, token: t };
        $cookieStore.put('user', currentUser);
    };

    return {
        isLoggedIn: function() {
            return currentUser.token != ''
        },

        register: function(user, success, error) {
            $http.post('/api/register', user).success(function(res) {
                changeUser(res);
                success();
            }).error(error);
        },
        login: function(user, success, error) {
            console.log(user);
            $http.post('/api/token-auth', user).success(function(res){
                changeUser(user.username, res.token);
                success({ username: user.username, token: res.token });
            }).error(error);
        },
        clear: function(success, error) {
            changeUser('', '');
        },

        user: currentUser
    };
});
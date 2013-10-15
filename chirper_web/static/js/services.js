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

app.factory('ChirpsService', function($http, $cookieStore){
        return {
            query: function() {
                console.log($cookieStore.get('user').token)
                $http.defaults.headers.post = { 'Authorization': 'Token ' + $cookieStore.get('user').token }
                console.log($http.defaults.headers.post)
                $http.get('/api/chirps').success(function(res){
                    console.log(res);
                    return res;
                });
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
        var currentUser = { username: u, token: t };
        $cookieStore.put('user', currentUser);
    };

    return {
        isLoggedIn: function() {
            console.log(currentUser);
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
                console.log(res)
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
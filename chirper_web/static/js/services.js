var app = angular.module('chirper.api', ['ngCookies', 'ngResource'])

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
        logout: function(success, error) {
            changeUser('', '');
            // $http.post('/logout').success(function(){
            //     changeUser({
            //         username: '',
            //         role: userRoles.public
            //     });
            //     success();
            // }).error(error);
        },
        
        user: currentUser
    };
});
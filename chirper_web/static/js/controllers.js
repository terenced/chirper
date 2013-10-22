angular.module('chirper-app').controller({
    ContentController: function ($scope, ChirpsService){

        $scope.initProperties = function(){
            $scope.chirp = ""
            $scope.chirps = []
            $scope.invalid = true
        }

        $scope.initEvents = function(){
             $scope.$on('auth-loginConfirmed', function() {
                ChirpsService.getChirps().then(function(chirps) {
                    chirps.forEach(function(chirp){
                        $scope.chirps.push(chirp);
                    });
                });
            });

            $scope.$on('loggedOut', function() {
                $scope.chirps.splice(0, $scope.chirps.length);
                $scope.initProperties();
            });
        }

        $scope.init = function(){
            $scope.initProperties();
            $scope.initEvents();
        }

        $scope.change = function() {
            $scope.invalid = ($scope.chirp.length > 140 || $scope.chirp.length < 1)
        };

        $scope.createChirp = function () {
            res = ChirpsService.create($scope.chirp);
            $scope.chirp = ""
            $scope.getChirps()
        };

        $scope.getChirps = function(){
            ChirpsService.getChirps().then(function(chirps) {
                chirps.forEach(function(chirp){
                    $scope.chirps.push(chirp);
                });
            });
        }
    }
});

angular.module('chirper-app').controller({
    LoginController: function ($scope, $http, AuthService, $rootScope) {

        $scope.isLoggedIn = false;
        $scope.user = { username: '', token: '' };

        $scope.update = function() {
            $scope.isLoggedIn = AuthService.isLoggedIn();
            $scope.user = AuthService.getUser();

            if($scope.isLoggedIn) {
                $rootScope.$broadcast('auth-loginConfirmed');
            }
            else {
                $rootScope.$broadcast('auth-loginRequired');
            }
        }

        $scope.init = function () {
            AuthService.load();
            $scope.update();
        }

        $scope.login = function() {
            AuthService.login({
                username: $scope.username,
                password: $scope.password,
            },
            function(res) {
                $scope.update();
            },
            function(err) {
                $scope.update();
            });
        }

        $scope.logout = function() {
            AuthService.logout(function(res) {
                $rootScope.$broadcast('loggedOut');
                $scope.isLoggedIn = false;
                $scope.username = '';
                $scope.password = '';
                $scope.register_username = ''; 
                $scope.register_first_name = ''; 
                $scope.register_last_name = ''; 
                $scope.register_password = '';
                $scope.update();
            });
        }

        $scope.register_user = function() {
            var user = { 
                'username': $scope.register_username, 
                'first_name': $scope.register_first_name, 
                'last_name': $scope.register_last_name, 
                'password': $scope.register_password
            }
            console.log(user)
            AuthService.register(user,
                function(res) {
                    $scope.update();
                },
                function(err) {
                    console.log(err)
                    $scope.update();
                }
            );
        } 
    }
});
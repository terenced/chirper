angular.module('chirper-app').controller({
    ContentController: function ($scope, ChirpsService){

        $scope.chirp = ""
        $scope.chirps = []

        $scope.invalid = true

        $scope.init = function(){
            $scope.$on('auth-loginConfirmed', function() {
                ChirpsService.getChirps().then(function(chirps) {
                    chirps.forEach(function(chirp){
                        $scope.chirps.push(chirp);
                    });
                });
            });
        }

        $scope.change = function() {
            $scope.invalid = ($scope.chirp.length > 140 || $scope.chirp.length < 1)
        };

        $scope.createChirp = function () {
            var chirp = new ChirpsService();
            chirp.content = $scope.chirp;
            chirp.user_id = 1
            chirp.$save(function(response){
                $scope.chirps.push(response);
            });
        };
    }
});

angular.module('chirper-app').controller({
    LoginController: function ($scope, $http, AuthService, $rootScope) {

        $scope.isLoggedIn = false;

        $scope.update = function() {
            $scope.isLoggedIn = AuthService.isLoggedIn();

            if($scope.isLoggedIn) {
                $rootScope.$broadcast('auth-loginConfirmed');
            }
            else {
                $rootScope.$broadcast('auth-loginRequired');
            }
        }

        $scope.init = function () {
            AuthService.clear();
            $scope.update();
        }

        $scope.submit = function() {
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
    }
});
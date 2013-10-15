angular.module('chirper-app').controller({
    ContentController: function ($scope, ChirpsService){

        $scope.hi = "hi";
        $scope.chirp = ""
        $scope.chirps = []

        $scope.invalid = true

        // ChirpsService.query(function(response){
        //     $scope.chirps = response;
        // });

        $scope.change = function() {
            $scope.invalid = ($scope.chirp.length > 140 || $scope.chirp.length < 1)

            ChirpsService.query(function(response){
                $scope.$apply($scope.chirps = response);
            });
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
                console.log('auth-loginConfirmed');
                $rootScope.$broadcast('auth-loginConfirmed');
            }
            else {
                console.log('auth-loginRequired');
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
                console.log(res);
                $scope.isLoggedIn = true;
                $scope.update();
            },
            function(err) {
                console.log(err);
                $scope.isLoggedIn = false;
                $scope.update();
            });
        }
    }
});
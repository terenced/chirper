angular.module('chirper-app').controller({
    ContentController: function ($scope, ChirpsService){

        $scope.hi = "hi";
        $scope.chirp = ""
        $scope.chirps = []

        $scope.invalid = true

        ChirpsService.query(function(response){
            $scope.chirps = response;
        });

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
    LoginController: function ($scope, $http, AuthService) {

        $scope.isLoggedIn = false;
        $scope.init = function () {
            AuthService.logout()
            console.log("init");
            $scope.isLoggedIn = AuthService.isLoggedIn();
            console.log("init");
        }
        

        // $scope.isLoggedIn = function() {
        //     console.log("checking");
        //     AuthService.isLoggedIn();
        // }
        $scope.submit = function() {
            AuthService.login({
                username: $scope.username,
                password: $scope.password,
            },
            function(res) {
                console.log(res);
                $scope.isLoggedIn = true;
                //alert(res);
            },
            function(err) {
                console.log(err);
                $scope.isLoggedIn = false;
                //alert(res);
            });
        }
    }
});
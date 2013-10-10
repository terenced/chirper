function ChirpTimelineCtl($scope, ChirpsService){

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
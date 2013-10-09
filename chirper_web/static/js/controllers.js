function ChirpTimelineCtl($scope, ChirpTimeline){

    $scope.chirps = []

    ChirpTimeline.query(function(response){
        $scope.chirps = response;
    });


}
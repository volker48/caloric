angular.module('caloric.controllers').controller('SearchCtrl', ['$scope', '$http', '$log',
    function($scope, $http, $log) {
        $scope.searchRange = {startDate: moment().utc(), endDate: moment().utc()};

        $scope.dateRangeOptions = {timePicker: true, timeZone: 0, timePickerIncrement: 5};


        $scope.search = function(searchRange) {
            $http.get('/entry/search/', {params: {startDate: searchRange.startDate, endDate: searchRange.endDate}}).success(function(resp) {
                $log.info(resp);
                $scope.days = resp.results;
            }).error(function() {
                alertify.error('Could not search at this time :(');
            });
        };

    }]);
/**
 * Created by marcusmccurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('AuthCtrl', ['$scope', '$http', '$log',
function($scope, $http, $log) {
    $scope.accountData = {};

    $scope.loginData = {};

    $scope.login = function() {
        $log.info('Posting to /user/login/');
        $http.post('/user/login/', $scope.loginData).success(function(data) {
            $scope.user_id = data.success;
        });
    };

    $scope.createAccount = function() {
        $log.info($scope.accountData);
        $http.post('/user/signup/', $scope.accountData);
    }
}]);

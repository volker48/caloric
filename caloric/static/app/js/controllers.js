/**
 * Created by marcusmccurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('IndexCtrl', ['$scope', '$http',
    function ($scope) {


    }]);

caloricControllers.controller('LoginCtrl', ['$scope', '$http', '$log',
function($scope, $http, $log) {
    $scope.accountData = {};
    $scope.login = function() {
        $log.info('Posting to /user/login/');
        $http.post('/user/login/', $scope.accountData).success(function(data) {
            $scope.user_id = data.success;
        });
    };
}]);


caloricControllers.controller('SignupCtrl', ['$scope', '$http', '$log',
    function($scope, $http, $log) {
        $scope.accountData = {};

        $scope.createAccount = function() {
            $log.info($scope.accountData);
            $http.post('/user/signup/', $scope.accountData);
        }
    }]);

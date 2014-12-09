/**
 * Created by marcusmccurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('IndexCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $scope.login = function(email, password) {

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

/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('AppCtrl', ['$scope', 'AUTH_EVENTS',
    function($scope, AUTH_EVENTS) {
        $scope.currentUser = null;

        $scope.setCurrentUser = function(user) {
            $scope.currentUser = user;
        };

        $scope.$on(AUTH_EVENTS.loginSuccess, function(event, user) {
            $scope.setCurrentUser(user);
        });
    }]);

caloricControllers.controller('AuthCtrl', ['$scope', '$http', 'Login',

    function($scope, $http, $log) {
        $scope.accountData = {username: '', password: ''};

        $scope.loginData = {username: '', password: ''};

        $scope.login = Login.login;

        $scope.createAccount = function(accountData) {
            $log.info(accountData);
            $http.post('/user/signup/', accountData);
        }
    }]);


caloricControllers.controller('EntryCtrl', ['$scope', 'Entry',
    function($scope, Entry) {

    }]);



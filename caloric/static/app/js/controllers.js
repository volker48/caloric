/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('AppCtrl', ['$scope', 'AUTH_EVENTS', '$log',
    function($scope, AUTH_EVENTS, $log) {
        $scope.currentUser = null;

        $scope.setCurrentUser = function(user) {
            $log.info('Setting current user');
            $log.info(user);
            $scope.currentUser = user;
        };

        $scope.$on(AUTH_EVENTS.loginSuccess, function(event, user) {
            $scope.setCurrentUser(user);
        });
    }]);

caloricControllers.controller('AuthCtrl', ['$scope', '$http', '$log', 'Login', 'AUTH_EVENTS', '$location',

    function($scope, $http, $log, Login, AUTH_EVENTS, $location) {
        $scope.accountData = {username: '', password: ''};

        $scope.loginData = {username: '', password: ''};

        $scope.login = Login.login;

        $scope.createAccount = function(accountData) {
            $log.info(accountData);
            $http.post('/user/signup/', accountData);
        };

        $scope.$on(AUTH_EVENTS.loginSuccess, function(event, data) {
            $log.info('redirection to /entries/');
            $location.path('/entries/')
        });
    }]);


caloricControllers.controller('EntryCtrl', ['$scope', 'Entry', '$log',
    function($scope, Entry, $log) {
        $scope.newEntry = new Entry();

        $scope.date = {startDate: null, endDate: null};

        $scope.entries = [];

        Entry.query(function(resp) {
            $scope.entries = resp.entries;
        });

        $scope.saveEntry = function(newEntry) {
            newEntry.datetime = $scope.date;
            newEntry.$save().success(function(resp) {
                $scope.newEntry = new Entry();
                $scope.date = {startDate: null, endDate: null};
                $scope.entries.push(resp.entry);
            }).error(function(resp) {

            });
        };

    }]);



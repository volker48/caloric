angular.module('caloric.controllers').controller('AppCtrl', ['$scope', 'AUTH_EVENTS', '$log', '$window', 'Login', '$location',
    function($scope, AUTH_EVENTS, $log, $window, Login, $location) {
        $scope.currentUser = null;

        $scope.setCurrentUser = function(user) {
            $log.info('Setting current user');
            $log.info(user);
            $scope.currentUser = user;
        };

        $scope.logout = Login.logout;

        $scope.$on(AUTH_EVENTS.loginSuccess, function(event, user) {
            $scope.setCurrentUser(user);
        });

        $scope.$on(AUTH_EVENTS.logoutSuccess, function() {
            $scope.setCurrentUser(null);
            $location.path('/');
        });

        if ($window.localStorage.token !== undefined) {
            $scope.currentUser = Login.userFromToken($window.localStorage.token);
        }
    }]);
angular.module('caloric.controllers').controller('AuthCtrl', ['$scope', '$http', '$log', 'Login', 'AUTH_EVENTS', '$location',

    function($scope, $http, $log, Login, AUTH_EVENTS, $location) {
        $scope.accountData = {username: '', password: ''};

        $scope.loginData = {username: '', password: ''};

        $scope.login = Login.login;

        $scope.createAccount = function(accountData) {
            $log.info(accountData);
            $http.post('/user/signup/', accountData).success(function(resp) {
                alertify.success('Signup successful! Please login.');
                $scope.accountData = {username: '', password: ''}
            }).error(function() {
                alertify.error('Could not create your account at this time.');
            });
        };

        $scope.$on(AUTH_EVENTS.loginSuccess, function(event, data) {
            $log.info('redirection to /entries/');
            $location.path('/entries/')
        });
    }]);
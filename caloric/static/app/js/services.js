var caloricServices = angular.module('caloricServices', ['ngResource']);

//caloricServices.factory('User', ['$resource',
//    function($resource) {
//        return $resource('/users/:id/', {id: '@id'});
//    }]);


caloricServices.factory('Login', ['$http', '$window', '$rootScope', '$log', 'AUTH_EVENTS',

    function LoginFactory($http, $window, $rootScope, $log, AUTH_EVENTS) {

        var loginService = {};

        loginService.urlBase64Decode = function urlBase64Decode(str) {
            var output = str.replace('-', '+').replace('_', '/');
            switch (output.length % 4) {
                case 0:
                    break;
                case 2:
                    output += '==';
                    break;
                case 3:
                    output += '=';
                    break;
                default:
                    throw 'Illegal base64url string!';
            }
            return window.atob(output);
        };

        loginService.userFromToken = function userFromToken(token) {
            var encodedUser = token.split('.')[1];
            return JSON.parse(loginService.urlBase64Decode(encodedUser));

        };

        loginService.login = function login(loginData) {
            $log.info('Logging user in...');

            $http.post('/auth/', loginData).success(function(resp) {
                $window.sessionStorage.token = resp.token;
                var user = loginService.userFromToken(resp.token);
                $rootScope.$broadcast(AUTH_EVENTS.loginSuccess, user);
            });

        };

        return loginService;
    }]);
/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricApp = angular.module('caloricApp', [
    'ngRoute',
    'ngResource',
    'ngAnimate',
    'angular-lodash',
    'daterangepicker',
    'caloricControllers',
    'caloricConstants',
    'caloricServices'
]);


caloricApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'static/app/partials/index.html',
                controller: 'AuthCtrl'
            }).
            when('/user/settings/', {
                templateUrl: 'static/app/partials/settings.html'

            }).
            when('/entries/', {
                templateUrl: 'static/app/partials/entries.html',
                controller: 'EntryCtrl'
            }).
            when('/settings/', {
               templateUrl: 'static/app/partials/settings.html',
                controller: 'SettingsCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

caloricApp.config(['$resourceProvider', function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);


caloricApp.factory('authInterceptor', ['$rootScope', '$q', '$window', '$log',
    function ($rootScope, $q, $window, $log) {
        return {
            request: function (config) {
                config.headers = config.headers || {};
                if ($window.localStorage.token) {
                    config.headers.Authorization = 'Bearer ' + $window.localStorage.token;
                }
                return config;
            },
            responseError: function (rejection) {
                if (rejection.status === 401) {
                    // handle the case where the user is not authenticated
                    $log.error('Rejected!');
                }
                return $q.reject(rejection);
            }
        };
    }]);

caloricApp.config(function ($httpProvider) {
    $httpProvider.interceptors.push('authInterceptor');
});
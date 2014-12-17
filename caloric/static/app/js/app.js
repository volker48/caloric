/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricApp = angular.module('caloricApp', [
    'ngRoute',
    'ngResource',
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
            otherwise({
                redirectTo: '/'
            });
    }]);

caloricApp.config(['$resourceProvider', function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
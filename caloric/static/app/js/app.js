/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricApp = angular.module('caloricApp', [
    'ngRoute',
    'ngResource',
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
            otherwise({
                redirectTo: '/'
            });
    }]);

caloricApp.config(['$resourceProvider', function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
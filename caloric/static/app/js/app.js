/**
 * Created by marcusmccurdy on 12/6/14.
 */

var caloricApp = angular.module('caloricApp', [
    'ngRoute',
    'caloricControllers'
]);


caloricApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'static/app/partials/index.html',
                controller: 'IndexCtrl'
            }).
            when('/signup', {
               templateUrl: 'static/app/partials/create-account.html',
                controller: 'SignupCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);
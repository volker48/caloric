angular.module('caloric.controllers').controller('SettingsCtrl', ['$scope', 'User', '$log',
    function($scope, User, $log) {
        $scope.settings = User.get({userId: $scope.currentUser.id});

        $scope.update = function update(user) {
            user.$save({userId: $scope.currentUser.id}, function(resp) {
                $scope.currentUser.email = resp.email;
                $scope.currentUser.daily_calories = resp.daily_calories;
                alertify.success('Settings updated.');
            }, function() {
                alertify.error('Could not save settings.');
            });
        };
    }]);

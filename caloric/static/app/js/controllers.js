/**
 * Created by Marcus McCurdy on 12/6/14.
 */

var caloricControllers = angular.module('caloricControllers', []);


caloricControllers.controller('AppCtrl', ['$scope', 'AUTH_EVENTS', '$log', '$window', 'Login', '$location',
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

caloricControllers.controller('AuthCtrl', ['$scope', '$http', '$log', 'Login', 'AUTH_EVENTS', '$location',

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


caloricControllers.controller('EntriesCtrl', ['$scope', 'Entry', '$log',
    function($scope, Entry, $log) {
        var dt = moment().utc();
        $scope.newEntry = new Entry({datetime: {startDate: dt, endDate: dt}});

        $scope.entries = [];

        Entry.query(function(resp) {
            $scope.entries = resp.entries;
        });

        $scope.saveEntry = function saveEntry(newEntry) {
            newEntry.$save(function(resp) {
                $log.info('New Entry ' + resp.entry);
                var dt = moment().utc();
                $scope.newEntry = new Entry({datetime: {startDate: dt, endDate: dt}});
                $scope.entries.push(resp.entry);
            });
        };

        $scope.deleteEntry = function deleteEntry(id) {
            Entry.delete({entryId: id});
            $scope.entries = _.filter($scope.entries, function(entry) {return entry.id !== id;});
        };

        $scope.editEntry = function editEntry(entry) {
            $scope.originalEdit = entry;
            $scope.editingEntry = new Entry({id: entry.id, calories: entry.calories, text: entry.text, datetime: {startDate: moment(entry.datetime), endDate: moment(entry.datetime)}});
        };

        $scope.saveEdit = function saveEdit(entry) {
            entry.$save(function(resp) {
                $scope.originalEdit.text = resp.entry.text;
                $scope.originalEdit.calories = resp.entry.calories;
                $scope.originalEdit.datetime = resp.entry.datetime;
                delete($scope.editingEntry);
            });
        };

        $scope.cancelEdit = function cancelEdit() {
            $scope.editingEntry = null;
        };

    }]);


caloricControllers.controller('SettingsCtrl', ['$scope', 'User', '$log',
    function($scope, User, $log) {
        $scope.settings = User.get({userId: $scope.currentUser.id});

        $scope.update = function update(user) {
            user.$save({userId: $scope.currentUser.id}, function() {
                alertify.success('Settings updated.');
            }, function() {
                alertify.error('Could not save settings.');
            });
        };
    }]);
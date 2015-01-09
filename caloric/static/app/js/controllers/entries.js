angular.module('caloric.controllers').controller('EntriesCtrl', ['$scope', 'Entry', '$log',
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
            }, function() {
                alertify.error('Could not save entry!');
            });
        };

        $scope.deleteEntry = function deleteEntry(id) {
            Entry.delete({entryId: id}, function(resp) {
                $scope.entries = _.filter($scope.entries, function(entry) {return entry.id !== id;});
            }, function() {
                alertify.error('Could not delete entry');
            });

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
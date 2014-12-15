'use strict';

/* jasmine specs for controllers go here */
describe('Caloric controllers', function() {

    beforeEach(module('caloricApp'));

    describe('AppCtrl', function(){
        var scope, ctrl, $rootScope, AUTH_EVENTS;

        beforeEach(inject(function(_$rootScope_, $controller, _AUTH_EVENTS_) {
            $rootScope = _$rootScope_;
            scope = $rootScope.$new();
            ctrl = $controller('AppCtrl', {$scope: scope});
            AUTH_EVENTS = _AUTH_EVENTS_;
        }));

        it('should save currentUser to scope on loginSuccess', function() {
            expect(scope.currentUser).toBeNull();

            $rootScope.$broadcast(AUTH_EVENTS.loginSuccess, {id: 1, email: 'joe@gmail.com'});

            expect(scope.currentUser).not.toBeNull();
            expect(scope.currentUser).not.toBeUndefined();

            expect(scope.currentUser.id).toEqual(1);
            expect(scope.currentUser.email).toEqual('joe@gmail.com');
        });


    });
});
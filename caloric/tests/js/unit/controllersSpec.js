'use strict';

/* jasmine specs for controllers go here */
describe('Caloric controllers', function() {

    beforeEach(module('caloricApp'));

    describe('AuthCtrl', function(){
        var scope, ctrl, $httpBackend;

        beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.expectPOST('/user/login/').
                respond({'success': 1});

            scope = $rootScope.$new();
            ctrl = $controller('AuthCtrl', {$scope: scope});
        }));

        it('should fetch user id from xhr', function() {
            expect(scope.user_id).toBeUndefined();

            scope.login();

            $httpBackend.flush();

            expect(scope.user_id).toEqual(1);
        });


    });
});
'use strict';

/* jasmine specs for controllers go here */
describe('Caloric services', function () {

    beforeEach(module('caloricApp'));

    describe('Login', function () {
        var Login;

        var test_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJqb2VAZ21haWwuY29tIn0.dsl6AakjamWh6z0NycKtXej_D5GK9nViSDB6xwDB3hM';

        beforeEach(inject(function (_Login_) {
            Login = _Login_;
        }));

        it('should decode user properly', function () {
            var user = Login.userFromToken(test_token);
            expect(user).toEqual({id: 1, email: 'joe@gmail.com'});
        });

        describe('XHR Requests', function () {
            var $httpBackend, window;

            beforeEach(inject(function (_$httpBackend_, $window) {
                $httpBackend = _$httpBackend_;
                window = $window;

                $httpBackend.expectPOST('/auth/', {username: 'joe@gmail.com', password: 'abc123'}).
                    respond({'token': test_token})
            }));

            it('should fetch user from xhr', function () {
                expect(window.sessionStorage).not.toBeUndefined();

                Login.login({username: 'joe@gmail.com', password: 'abc123'});

                $httpBackend.flush();

                expect(window.sessionStorage.token).toEqual(test_token);
            });
        });
    });

    describe('Entry', function() {
        var Entry, $httpBackend;

        beforeEach(inject(function(_Entry_, _$httpBackend_) {
            Entry = _Entry_;
            $httpBackend = _$httpBackend_;
        }));

        it('should GET /entry/', function() {
           $httpBackend.expectGET('/entry/').respond({entries: [{id: 1, text: 'Steak', calories: 500}, {id: 2, text: 'Eggs', calories: 300}]});

            var entries;
            Entry.query(function(resp) {
                entries = resp.entries;
            });

            $httpBackend.flush();

            expect(entries.length).toEqual(2);
        });


    });
});
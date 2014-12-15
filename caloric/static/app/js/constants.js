var caloricConstants = angular.module('caloricConstants', []);


caloricConstants.constant('AUTH_EVENTS', {
    loginSuccess: 'login-success',
    loginFailed: 'login-failed',
    logoutSuccess: 'logout-success',
    notAuthenticated: 'not-authenticated',
    notAuthorized: 'not-authorized'
});
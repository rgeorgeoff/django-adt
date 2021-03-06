(function() {
    'use strict';

    angular.module('auth').factory('auth', [
        'common', '$auth', '$http', 'Session',
        function(common, $auth, $http, Session) {

            var _currentUser = null;

            var service = {
                storeSession: storeSession,
                currentUser: Session.currentUser
            };

            angular.extend(service, $auth);

            return service;
            /////////////////////

            function storeSession() {
                return $http.get('/api/users/profile/')
                    .then(function(response) {
                        var user = response.data;
                        console.log(user);
                        Session.create(
                            user.displayName,
                            user.email,
                            user.permissions
                        );
                    }).catch(function(error) {
                        common.exception.catcher(error);
                    });
            }

        }]);
}());
(function (ng) {
    var mod = ng.module('managerModule');

    mod.service('managerService', ['$http', 'managerContext', function ($http, context) {

        this.registerManager = function (data) {
            return $http({
                method: 'POST',
                url: '/register/',
                data:data
            });
        };

    }]);
})(window.angular);
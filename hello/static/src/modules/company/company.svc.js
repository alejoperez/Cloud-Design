(function (ng) {
    var mod = ng.module('companyModule');

    mod.service('companyService', ['$http', 'companyContext', function ($http, context) {

        this.getProjects = function (id) {
            return $http({
                method: 'GET',
                url: '/company/'+id
            });
        };

    }]);
})(window.angular);
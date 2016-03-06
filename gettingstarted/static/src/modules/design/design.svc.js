(function (ng) {
    var mod = ng.module('designModule');

    mod.service('designService', ['$http', 'designContext', function ($http, context) {

        this.getDesigns = function (projectId) {
            return $http({
                method: 'GET',
                url: '/getDesigns/'+projectId
            });
        };

    }]);
})(window.angular);
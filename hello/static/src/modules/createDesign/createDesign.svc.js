(function (ng) {
    var mod = ng.module('createDesignModule');

    mod.service('createDesignService', ['$http', 'createDesignContext', function ($http, context) {

        this.createDesign = function (data) {
            return $http({
                method: 'POST',
                url: '/design',
                data: data
            });
        };

    }]);
})(window.angular);
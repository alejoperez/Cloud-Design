(function (ng) {
    var mod = ng.module('createDesignModule');

    mod.service('createDesignService', ['$http', 'createDesignContext', function ($http, context) {

        this.createDesign = function (data) {
            return $http({
                method: 'POST',
                url: 'http://ec2-52-24-205-238.us-west-2.compute.amazonaws.com/design',
                data: data
            });
        };

    }]);
})(window.angular);

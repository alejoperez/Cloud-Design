(function (ng) {
    var mod = ng.module('createDesignModule');



    mod.controller('createDesignCtrl', ['$scope', 'createDesignService', function ($scope, createDesignService) {

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.createDesign = function () {
            return createDesignService.createDesign({
                'designer_name':angular.element('#designer_name').val(),
                'designer_last_name':angular.element('#designer_last_name').val(),
                'designer_email':angular.element('#designer_email').val(),
                'price':angular.element('#price').val(),
                'imageFile':angular.element('#fileString').val(),
                'project_pk':1
            }).then(function (response) {
                console.log(response);
                $scope.message = response.data;
            }, responseError);
        };

    }]);
})(window.angular);

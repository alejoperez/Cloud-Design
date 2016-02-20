(function (ng) {
    var mod = ng.module('managerModule');

    mod.controller('managerCtrl', ['$scope', 'managerService', '$window', function ($scope, managerService, $window) {

        function responseError(response) {
            console.log(response);
        }

        /*
        this.getIndependents = function () {
            return managerService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };*/

        this.registerManager = function(){
            if(angular.element('#password').val() != angular.element('#confirm_password').val()){
                $window.alert("The password fields don't match");
                return;
            }
            return managerService.registerManager({
                'company':angular.element('#company').val(),
                'email':angular.element('#email').val(),
                'password':angular.element('#password').val()
            }).then(function (response) {
                $window.location.href = '/#/independents';
            }, responseError);
        };

        /*
        this.getJobs = function () {
            return independentsService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);
        };*/

    }]);
})(window.angular);

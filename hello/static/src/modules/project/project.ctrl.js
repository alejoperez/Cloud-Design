(function (ng) {
    var mod = ng.module('projectModule');

    mod.controller('projectCtrl', ['$scope', 'projectService', '$window', function ($scope, projectService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.getProjects = function () {
            return projectService.getProjects().then(function (response) {
                $scope.projects = response.data.proyectos;
                console.log("asadasda"+response.data.proyectos);
            }, responseError);
        };



    }]);
})(window.angular);

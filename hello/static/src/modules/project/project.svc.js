(function (ng) {
    var mod = ng.module('projectModule');

    mod.service('projectService', ['$http', 'projectContext', function ($http, context) {

    this.getProjects = function () {
                return $http({
                    method: 'GET',
                    url: '/project/'
                });
    };

    this.deleteProject = function (id) {
                return $http({
                    method: 'DELETE',
                    url: '/project/',
                    data:{
                        pk:id
                    }
                });
        };
    }]);


})(window.angular);
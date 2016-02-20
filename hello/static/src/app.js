(function (ng) {

    var helpApp = ng.module('helpApp', [
        'ngRoute',
        'managerModule',
        'profileModule',
        'mainModule',
        'loginModule',
        'commentsModule',
        'detailModule'
        'projectModule'
    ]);

    helpApp.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/independents', {
                templateUrl: 'static/src/modules/manager/independents.tpl.html',
                controller: 'managerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/profile', {
                templateUrl: 'static/src/modules/profile/profile.tpl.html',
                controller: 'profileCtrl',
                controllerAs: 'ctrl'
            })
            .when('/login', {
                templateUrl: 'static/src/modules/login/login.tpl.html',
                controller: 'loginCtrl',
                controllerAs: 'ctrl'
            })
            .when('/register', {
                templateUrl: 'static/src/modules/manager/registration.tpl.html',
                controller: 'managerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/comments/:idIndependent', {
                templateUrl: 'static/src/modules/comments/comments.tpl.html',
                controller: 'commentsCtrl',
                controllerAs: 'ctrl'
            })
            .when('/detail/:idIndependent', {
                templateUrl: 'static/src/modules/detail/detail.tpl.html',
                controller: 'detailCtrl',
                controllerAs: 'ctrl'
            })
            .when('/project', {
                templateUrl: 'static/src/modules/project/project.tpl.html',
                controller: 'projectCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/independents');



    }]);
})(window.angular);

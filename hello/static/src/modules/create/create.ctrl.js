/**
 * Created by IvanGarcia on 20/02/2016.
 */
(function (ng) {
    var mod = ng.module('createModule');

    mod.controller('createCtrl', ['$scope', 'createService', '$window', function ($scope, createService, $window) {

        function responseError(response) {
            console.log(response);
        }

          this.registerManager = function(){
            return createService.registerProject({
                'nombre':angular.element('#nombre').val(),
                'descripcion':angular.element('#descripcion').val(),
                'precio':angular.element('#precio').val(),
                'imagen':angular.element('#imagen').val()

            }).then(function (response) {
                $window.location.href = '/#/project';
            }, responseError);
        };
    }]);
})(window.angular);

(function (ng) {
    var mod = ng.module('editModule');

    mod.controller('editCtrl', ['$scope', 'editService', '$window', function ($scope, editService, $window) {
        $scope.objeto= {};

        function responseError(response) {
            console.log(response);
        }

    }]);
})(window.angular);

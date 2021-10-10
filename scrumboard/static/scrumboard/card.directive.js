(function(){
    'use strict';

    angular.module('scrumboard.demo')
        .directive('scrumboardCard', CardDirective);
        // scrumboardCard directive is scrumboard-card in home.html
    function CardDirective(){
        return{
            templateUrl:'/static/scrumboard/card.html',
            restrict: 'E'
        };
    }

})();
 (function(){
            'use strict';
            angular.module('scrumboard.demo', [])
                .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

          function ScrumboardController($scope,$http){
            $scope.add = function(list, title){
                var card = {
                    title: title
                };
                list.cards.push(card);
            };

            // get angular code for HTTP GET
            $scope.data = []; // init data
            // next, get from DB, then waits for response
            $http.get('/scrumboard/lists').then(function(response){
                // copy data from REST call
                $scope.data = response.data;
            });


          }

        }());
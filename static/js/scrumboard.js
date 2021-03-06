 (function(){
            'use strict';
            angular.module('scrumboard.demo', [])
                .controller('ScrumboardController', ['$scope', '$http', ScrumboardController]);

          function ScrumboardController($scope,$http){
            $scope.add = function(list, title){
                var card = {
                    // foreign key from JS below:
                    list: list.id, // now we have FK
                    title: title
                };
                // POST to server
                $http.post('/scrumboard/cards/', card)
                .then(function(response){
                   // only push after reponse OK
                   // from server, id is stored
                   list.cards.push(response.data);
                },
                // error handler below is second arg
                function(){
                  alert("Could not create card!");
                });
            };

            $scope.login = function(){
                $http.post('/auth_api/login/',
                {username: 'fmoldovan', password: '0000'});
            }

            // get angular code for HTTP GET
            $scope.data = []; // init data
            // next, get from DB, then waits for response
            $http.get('/scrumboard/lists/').then(function(response){
                // copy data from REST call
                $scope.data = response.data;
            });


          }

        }());
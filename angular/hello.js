var hello = angular.module('hello', []);

hello.controller('HelloController', function($scope){
	$scope.message = {text:"Hello bob"};

});
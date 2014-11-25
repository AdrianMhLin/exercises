var todoApp = angular.module('todoApp', []);


todoApp.controller('TodoController', function($scope){
	$scope.message = "THIS IS A MESSAGE";

	todos = [
		{product:"sugar", price:20, checked:true},
		{product:"spice", price:30, checked:false},
		{product:"everything nice", price:50, checked:false}
	];

	$scope.todos = todos;
});


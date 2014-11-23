var newApp = angular.module('newApp', []);

newApp.controller('OctopusController', function($scope){

	$scope.message = "There are many octopuses!";

	octopuses = [
		{name: "bob", color:"brown", price:5},
		{name: "carol", color:"grey", price:15},
		{name: "Optimus Prime", color:"red", price:25}
	];
	
	$scope.octopuses = octopuses;


});

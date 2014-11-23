var myApp = angular.module("myApp", []);

myApp.factory("Greeting", function(){
	return {message:"I'm a test"}
});

myApp.controller('PetController', function($scope){
	

	var pets = [
		{type: "dog", price: 50},
		{type: "cat", price: 65},
		{type: "bird", price: 35},
		{type: "octopus", price: 85}
	];
	$scope.pets = pets;

	$scope.message = "pets for sale!";

});

myApp.controller('SecondController', function($scope, Greeting){
	$scope.greeting = Greeting;
});


var candyShop = angular.module('candyShop', []);

candyShop.controller('CandyController', function($scope){

	$scope.message = "this is the fucking message"

	candies = [
		{type:"chocolate", price:5},
		{type:"toffee", price:4},
		{type:"gummy", price:3}
	];

	$scope.candies = candies
});


var myApp = angular.module("coolApp", []);

coolApp.factory("Data", function(){
	return {message:"I'm data from a service"}
});

function MainController($scope, Data){
	$scope.data = Data
	$scope.product = {
		price: 1.5,
		name: "Poland Spring Water Bottle"
	};
}

function SecondController($scope){
	$scope.product = {
		price: 5,
		name: "chicken over rice"
	};
}
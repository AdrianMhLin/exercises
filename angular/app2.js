
var myApp = angular.module("myApp", []);

myApp.factory("Data", function(){
	return {message:"I'm data from a service"}
});

function MainController($scope, Data){
	$scope.data = Data;
}

function SecondController($scope, Data){
	$scope.data = Data;
}
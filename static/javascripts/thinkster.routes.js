(function() {
	'use strict';

	angular.module('thinkster.routes').config(config);

	config.$inject = [ '$routeProvider' ];

	/**
	 * @name config
	 * @desc Define valid application routes
	 */
	function config($routeProvider) {
		$routeProvider.when('/register', {
			controller : 'RegisterController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/authentication/register.html'

		}).when('/login', {
			controller : 'LoginController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/authentication/login.html'
		}).when('/shop', {
			controller : 'ProductsController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/ecomm/products.html'
				
		}).when('/orders', {
			controller : 'CartController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/ecomm/orders.html'
		}).when('/orders/:id', {
			controller : 'CartController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/ecomm/placeOrder.html'
	
		}).when('/cart', {
			controller : 'CartController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/ecomm/placeOrder.html'
		
		}).when('/+:username/settings', {
			controller : 'ProfileSettingsController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/profiles/settings.html'

		}).when('/+:username', {
			controller : 'ProfileController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/profiles/profile.html'

		}).when('/', {
			controller : 'IndexController',
			controllerAs : 'vm',
			templateUrl : '/static/templates/layout/index.html'
		}).otherwise('/');

	}
})();
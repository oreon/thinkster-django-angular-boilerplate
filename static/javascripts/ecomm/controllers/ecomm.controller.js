/**
 * ProductsController
 * 
 * @namespace thinkster.products.controllers
 */
(function() {
	'use strict';

	angular.module('thinkster.ecomm.controllers').controller(
			'ProductsController', ProductsController);

	ProductsController.$inject = [ '$scope', 'Products' ];

	/**
	 * @namespace ProductsController
	 */
	function ProductsController($scope, Products) {
		var vm = this;

		vm.products = [];

		activate();

		/**
		 * @name activate
		 * @desc Actions to be performed when this controller is instantiated
		 * @memberOf thinkster.products.controllers.ProductsController
		 */
		function activate() {
			Products.all().then(postsSuccessFn, postsErrorFn);

			function postsSuccessFn(data, status, headers, config) {
				vm.products = data.data;
			}

			function postsErrorFn(data, status, headers, config) {
				// Snackbar.error(data.error);
			}

		}

		function addToCart(product) {

		}

	}
})();

/**
 * ProductsController
 * 
 * @namespace thinkster.products.controllers
 */
(function() {
	'use strict';

	angular.module('thinkster.ecomm.controllers').controller('CartController',
			CartController);

	CartController.$inject = [ '$scope', '$routeParams', '$location',
			'AllProducts', 'Checkout', 'Customers', 'CustomerOrders' ];

	/**
	 * @namespace ProductsController
	 */
	function CartController($scope, $routeParams, $location, AllProducts,
			Checkout, Customers, CustomerOrders) {
		var vm = this;

		vm.products = [];
		vm.customers = [];
		vm.customerOrders = [];

		vm.order = {};
		/*
		 * vm.items = [ { product : "http://localhost:8000/api/v1/products/1/",
		 * qty : 10, price : 20 }, {
		 * 
		 * product : "http://localhost:8000/api/v1/products/2/", qty : 1, price :
		 * 100 } ];
		 * 
		 * //vm.order.items = vm.items;
		 */
		activate();

		/**
		 * @name activate
		 * @desc Actions to be performed when this controller is instantiated
		 * @memberOf thinkster.products.controllers.ProductsController
		 */
		function activate() {

			// alert("hi all ");

			Customers.query(function(data) {
				angular.forEach(data, function(item) {
					if (angular.isArray(item))
						vm.customers = item;
				});
			});

			AllProducts.query(function(data) {
				angular.forEach(data, function(item) {
					if (angular.isArray(item))
						vm.products = item;
				});
			});// .then(postsSuccessFn,
			// postsErrorFn);

			console.log(vm.products);

			var id = $routeParams.id;

			if (id) {
				
				
				if (id > 0) {
					vm.order = CustomerOrders.get({
						id : $routeParams.id
					});
					
					
				}else{
					vm.order  =  new CustomerOrders;
					vm.order.orderItems = [];
				}

			} else {
				CustomerOrders.query({page:8}, function(data) {
					angular.forEach(data, function(item) {
						console.log(item);
						if (angular.isArray(item))
							vm.customerOrders = item;
					});
				});
			}

			function postsSuccessFn(data, status, headers, config) {
				// data.data;
			}

			function postsErrorFn(data, status, headers, config) {
				// Snackbar.error(data.error);
			}
			;

		}

		vm.addNew = function() {
			var item = {}
			vm.order.orderItems.push(item);
		}

		function edit(activity) {
			var selectedActivity = activity;
			console.log(selectedActivity);
		}

		vm.remove = function(index) {
			alert("remvoing " + index);
			/*
			activityId = activity.id; // the activity id

			var i = 0;
			for ( var item in $scope.activities) {
				if ($scope.activities[item].id == activityId)
					break;
				i++;
			}*/

			vm.order.orderItems.splice(index, 1);
		}

		vm.placeOrder = function() {
			alert("in order")
			// vm.order.orderItems = vm.items;
			console.log(vm.order.orderItems);
			vm.order.$save(/*
								 * , function(data) { }
								 */);

			$location.url('/orders');

		}

	}
})();
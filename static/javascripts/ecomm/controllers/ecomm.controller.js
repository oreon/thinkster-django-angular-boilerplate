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

	CartController.$inject = [ '$scope', 'AllProducts', 'Checkout', 'Customers' ];

	/**
	 * @namespace ProductsController
	 */
	function CartController($scope, AllProducts, Checkout, Customers) {
		var vm = this;

		vm.products = [];
		vm.customers = [];

		// vm.orderItems = [];

		vm.order = {
			"description" : "THIS IS ASWESOME",
			"order" : "" 
		};

		vm.items = [ {
			product : "http://localhost:8000/api/v1/products/1/",
			qty : 10,
			price : 20
		}, {

			product :  "http://localhost:8000/api/v1/products/2/",
			qty : 1,
			price : 100
		} ];

		vm.order.items = vm.items;

		activate();

		/**
		 * @name activate
		 * @desc Actions to be performed when this controller is instantiated
		 * @memberOf thinkster.products.controllers.ProductsController
		 */
		function activate() {
			vm.products = AllProducts.query();//.then(postsSuccessFn, postsErrorFn);

			function postsSuccessFn(data, status, headers, config) {
				 //data.data;
			}

			function postsErrorFn(data, status, headers, config) {
				// Snackbar.error(data.error);
			}
			
			vm.customers = Customers.query(function (data){
				
			})

		}

		function addToCart(product) {

		}

		vm.addNew = function() {
			/*
			 * var updatedActivities = { id : 6433, name : "Call", points : 5 };
			 */

			var item = {}
			alert('Called')
			vm.items.push(item);
		}

		function edit(activity) {
			var selectedActivity = activity;
			console.log(selectedActivity);
		}

		vm.remove = function(activity) {
			activityId = activity.id; // the activity id

			var i = 0;
			for ( var item in $scope.activities) {
				if ($scope.activities[item].id == activityId)
					break;
				i++;
			}

			$scope.activities.splice(i, 1);
		}

		vm.placeOrder = function() {
			//alert(vm.order.order)
			vm.order.orderItems = vm.items;
			console.log(vm.order.orderItems);
			Checkout.placeOrder(vm.order);
		}

	}
})();
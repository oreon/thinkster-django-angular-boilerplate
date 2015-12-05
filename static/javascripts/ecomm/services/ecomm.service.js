

var Customers = angular.module('thinkster.ecomm.services').factory('Customers', function($resource) {
	return $resource('/api/v1/customers/:id', {id:'@id'},{
		  query : {
			    method : 'GET',
			    isArray : false
			  }
			});
});


var AllProducts = angular.module('thinkster.ecomm.services').factory('AllProducts', function($resource) {
	return $resource('/api/v1/allProducts/:id', {id:'@id'},{
		  query : {
			    method : 'GET',
			    isArray : false
			  }
			});
});


var CustomerOrders = angular.module('thinkster.ecomm.services').factory('CustomerOrders', function($resource) {
	var res =  $resource('/api/v1/customerOrders/:id/', {id:'@id', page:'@page'},{
		  query : {
			    method : 'GET',
			    isArray : false
			  },
		'update': { method:'PUT' },
		'create': { method:'POST' }
	});
	
	res.prototype.$save = function() {
	    if (this.id) {
	        return this.$update();
	    } else {
	        return this.$create();
	    }
	};
	
	return res;
});




/**
 * Posts
 * 
 * @namespace thinkster.posts.services
 */
(function () {
  'use strict';

  angular
    .module('thinkster.ecomm.services')
    .factory('Products', Products);

  Products.$inject = ['$http'];

  function Products($http) {
	  
    var Products = {
      all: all,
      create: create,
      get: get
    };

    return Products;

    // //////////////////

    /**
	 * @name all
	 * @desc Get all Posts
	 * @returns {Promise}
	 * @memberOf thinkster.posts.services.Posts
	 */
    function all() {
      return $http.get('/api/v1/products/');
      // return $http.get('/api/v1/posts/');
    }


    /**
	 * @name create
	 * @desc Create a new Post
	 * @param {string}
	 *            content The content of the new Post
	 * @returns {Promise}
	 * @memberOf thinkster.posts.services.Posts
	 */
    function create(content) {
      return $http.post('/api/v1/products/', {
        content: content
      });
    }

    /**
	 * @name get
	 * @desc Get the Posts of a given user
	 * @param {string}
	 *            username The username to get Posts for
	 * @returns {Promise}
	 * @memberOf thinkster.posts.services.Posts
	 */
    function get(username) {
      return $http.get('/api/v1/accounts/' + username + '/posts/');
    }
  }
})();



(function () {
	  'use strict';

	  angular
	    .module('thinkster.ecomm.services')
	    .factory('Checkout', Checkout);

	  Checkout.$inject = ['$http'];

	  /**
		 * @namespace Posts
		 * @returns {Factory}
		 */
	  function Checkout($http) {
		  
	    var Checkout = {
	      placeOrder
	    };

	    return Checkout;
	    
	    function placeOrder(order) {
	    	return $http.post('/api/v1/customerOrders/',order);
	    }
	    
	    /*
		 * function placeOrder2() { return $http.post('/api/v1/customerOrders/', {
		 * "orderItems": [ { "product": "2", "qty": 1, // "customerOrder": //
		 * "http://localhost:8000/api/v1/customerOrders/1/" } ], "description":
		 * "this is a good one", "order": "1" }); }
		 */
	  }
})();	  
	  
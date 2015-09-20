(function () {
  'use strict';

  angular
    .module('thinkster.ecomm', [
      'thinkster.ecomm.controllers',
      //'thinkster.posts.directives',
      'thinkster.ecomm.services'
    ]);

  angular
    .module('thinkster.ecomm.controllers', []);

  //angular.module('thinkster.posts.directives', ['ngDialog']);

  angular
    .module('thinkster.ecomm.services', []);
})();
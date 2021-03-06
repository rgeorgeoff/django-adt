// Init the application configuration module for AngularJS application
var ApplicationConfiguration = (function() {
    'use strict';

	// Init module configuration options
	var applicationModuleName = 'app';
	var applicationModuleVendorDependencies = [
		'ngResource',
        'ngMessages',
		'ngAnimate',
        'templates',
        'ui.router',
		'SwampDragonServices',
		'satellizer',
		'LocalStorageModule',
		'ui.bootstrap',
		'mgcrea.ngStrap',
        'rx',
		'angularMoment',
		//'sun.scrollable',
		'ncy-angular-breadcrumb',
		'angular-loading-bar',
		'restangular',
		'js-data',
		//'ui.tree',
		'ngFitText',
		'toastr',
		'ee.$http.CaseConverter',

        //These aren't in webpack yet and require the evil jQuery
        'sun.scrollable',
        'infinite-scroll'
	];

	// Add a new vertical module
	var registerModule = function(moduleName, dependencies) {
		// Create angular module
		angular.module(moduleName, dependencies || []);

		// Add the module to the AngularJS configuration file
		angular.module(applicationModuleName).requires.push(moduleName);
	};

	return {
		applicationModuleName: applicationModuleName,
		applicationModuleVendorDependencies: applicationModuleVendorDependencies,
		registerModule: registerModule
	};
})();

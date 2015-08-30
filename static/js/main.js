require.config({
  waitSeconds: 300,

  paths: {
    "jquery": 'vendor/jquery-1.11.3',
    // "bootstrap": 'vendor/bootstrap-min',
    "bootstrap": 'vendor/bootstrap',
    "underscore": 'vendor/underscore',
    "backbone": 'vendor/backbone',
    "backbone-deep-model": 'vendor/backbone-deep-model',
    "backbone-forms": 'vendor/backbone-forms',
    "bootstrap-forms": 'vendor/bootstrap-forms-min',
    "bootstrap-forms-modal": 'vendor/backbone.bootstrap-modal',
    "list": 'vendor/list',
    // 'handlebars': '../vendor/handlebars-runtime',
    "App": './app'
  },

  shim: {
    "bootstrap-forms": {
      deps: ['jquery', 'bootstrap']
    },

    bootstrap: {
      deps: ['jquery']
    },

    underscore: {
      exports: '_'
    },

    "backbone-deep-model": {
      deps: ['jquery', 'underscore', 'backbone'],
      exports: 'DeepModel'
    },

    "bootstrap-forms-modal": {
      deps: ['jquery', 'underscore', 'backbone', 'bootstrap'],
      exports: 'Backbone.BootstrapModal'
    },

    backbone: {
      deps: ['underscore', 'jquery'],
      exports: 'Backbone'
    },

    list: {
      deps: ['jquery', 'underscore', 'backbone', 'backbone-forms', 'backbone-deep-model', 'bootstrap-forms-modal'],
      exports: 'BackboneForms'
    },

    // 'handlebars': {
    //   exports: 'Handlebars'
    // },
  },
});

require(['jquery'], function($) {
    $(function() {
      require(['App'], function(App){
        App.init();
      });
    });
});


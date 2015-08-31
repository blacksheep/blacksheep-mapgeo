define(["backbone","backbone-deep-model", "./Calendar"], function(Backbone, DeepModel){
      var Calendar = Backbone.DeepModel.extend({
        urlRoot: 'api/v1/calendar',

        initialize: function () {

        },

        defaults: {
        },

        schema: {
          dates: {
            type: 'List',
            itemType: 'Date',
            validators: ['required']
          },
        },
      });

  return Calendar;
})


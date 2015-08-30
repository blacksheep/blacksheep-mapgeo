define(["backbone","backbone-deep-model", "bootstrap-forms-modal"], function(Backbone, DeepModel){
  var Location = Backbone.Model.extend({
    urlRoot: 'api/free/location/',
    initialize: function () {

    },

    defaults: {
      latitude: "",
      longitude: "",
      radius: "5",
    },

    schema: {
      latitude: {
        type: 'Text',
        validators: ['required']
      },
      longitude: {
        type: 'Text',
        validators: ['required']
      },
      radius: {
        type: 'Number',
        validators: ['required']
      },
    },
  });

  return Location;
})

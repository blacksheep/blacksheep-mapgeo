define(["backbone","backbone-deep-model"], function(Backbone, DeepModel){
      var Address = Backbone.Model.extend({
        urlRoot: 'api/v1/address',

        initialize: function () {

        },

        defaults: {
          zipCode: "",
          state: "",
          city: "",
        },

        schema: {
          zipCode: {
            type: 'Number',
            validators: ['required']
          },
          State: {
            type: 'Select',
            options: ["CA"],
            validators: ['required']
          },
          city: {
            type: 'Text',
            validators: ['required']
          },

          // 'author.id': 'Number',
          // 'author.name.firstName': 'Text'
        },
        toString: function(){
          return 'hello world';
        }
      });

  return Address;
})


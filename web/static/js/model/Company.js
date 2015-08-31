define(["backbone","backbone-deep-model", "./Address", "./Calendar", "bootstrap-forms-modal"], function(Backbone, DeepModel, Address, Calendar){
  var Company = Backbone.Model.extend({
    urlRoot: 'api/v1/company',

    initialize: function () {

    },

    defaults: {
      // zipCode: "",
      // state: "",
      // city: "",
      email: "",
      category: "",
      phone: "",
      webSite: "",
      program: ""
      // address: "",
      // officeHour:"",
    },

    schema: {
      address: {
        // type: 'NestedModel',
        // model: Address,
        type: 'List',
        itemType:'NestedModel',
        model: Address,
        itemToString: function(val){
          return 'hello world itemToString ' + val;
        }
        // validators: ['required']
      },
      // zipCode: {
      //   type: 'Number',
      //   validators: ['required']
      // },
      // state: {
      //   type: 'Select',
      //   options: ["CA"],
      //   validators: ['required']
      // },
      category: {
        type: 'Text',
        validators: ['required']
      },
      // city: {
      //   type: 'Text',
      //   validators: ['required']
      // },
      phone: {
        type: 'Number',
        validators: ['required']
      },
      webSite: {
        type: 'Text'
      },
      officeHour:{
        type: 'NestedModel',
        model: Calendar,
        // validators: ['required']
      },
      program: {
        type: 'Text'
      },
      email: {
        validators: ['required', 'email']
      },
      // 'author.id': 'Number',
      // 'author.name.firstName': 'Text'
    },
  });

  return Company;
})

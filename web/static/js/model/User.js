define(["backbone"], function(Backbone){
  var User = Backbone.Model.extend({
    schema: {
      title:      { type: 'Select', options: ['Mr', 'Mrs', 'Ms'] },
      name:       'Text',
      email:      { validators: ['required', 'email'] },
      birthday:   'Date',
      password:   'Password',
      // address:    { type: 'NestedModel', model: Address },
      notes:      { type: 'List', itemType: 'Text' }
    },
  });

  return User;
})

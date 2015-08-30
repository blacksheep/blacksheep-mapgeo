define(["./model/User", "backbone", "list"], function(User, Backbone, List){

  var App = {
    init: function(){
      var user = new User();

      var form = new Backbone.Form({
        model: user,
        submitButton: "Submit"
      }).render();

      $('body').append(form.el);
    }
  };

  return App;
});




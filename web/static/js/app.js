define(["./model/Location", "backbone", "underscore", "backbone-deep-model","list"], function(Location, Backbone, _, DeepModel, List){

  var App = {
    init: function(){
      var location = new Location();
      var form = new Backbone.Form({
        model: location,
      }).render({
        fieldsets: 'fieldsets'
      });

      $('#form').append(form.el);

      $('.submit').click(function() {
        if( !!form.validate() ){
          console.log("ERRORS EXIST");
        } else {
          location.save();
        }
      });
    }
  };

  return App;
});



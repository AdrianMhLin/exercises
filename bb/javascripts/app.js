var Octopus = Backbone.Model.extend({
	initialize: function(){
		console.log("boom! new octopus initialised!");
	}
});

var OctopusCollection = Backbone.Collection.extend({
	initialize: function(){
		console.log("zoom! a swarm of octopuses appears!");
	}
});

var OctopusView = Backbone.View.extend({
	initialize: function(){
		console.log("this is how an octopus looks");
		this.listenTo( this.model, 'change', this.render );
		this.listenTo( this.model, 'destroy', this.remove );
	},
	render: function(){
		var entrails = "";
		entrails += "<h1 class='name-octopus'>" + this.model.get('name') + "</h1>";
		entrails += "<button class='delete-octopus' id='delete-'" + this.model.get('name') + "'>delete " + this.model.get('name') + "</button>"

		this.$el.html(entrails);
	}, 

	events: {
		"click .delete-octopus" : "destroy",
		"dblclick .name-octopus" : "update"
	},

	destroy: function(){
		
		console.log(this.model);
		this.model.destroy();
		this.remove();
	},

	update: function(){
		var newName = prompt('edit name');
		this.model.set('name', newName);
	}


});

var OctopusListView = Backbone.View.extend({
	initialize: function(){
		console.log("this is how many octopuses look!");
	}
});




$(function(){

	$('#btn-octopus').on('click', function(){
		console.log("clicked!");
		var octoName = $('#input-octopus').val();
		var octoPus = new Octopus({"name": octoName});
		var octoView = new OctopusView({model: octoPus});
		octoView.render();

		$('#octopus-nest').append(octoView.el);
	});

});
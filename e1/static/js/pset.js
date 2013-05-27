/**
 * Model for a generic problem
 */
var Problem = Backbone.Model.extend({
});

/**
 * Model for a collection of problems
 */
var ProblemCollection = Backbone.Collection.extend({
    model: Problem
});

/**
 * View representing a single pset problem
 */
var ProblemView = Backbone.View.extend({
    className: 'problem',

    initialize: function() {
        this.template = _.template($(this.elTemplate).html());
        this.render();
    },

    render: function() {
        this.$el.html(this.template({ problem: this.model }));
        return this;
    }
});

/**
 * View representing a true/false problem
 */
var TFProblemView = ProblemView.extend({
    elTemplate: '#tf-problem-template',
});

/**
 * View representing a multiple choice problem
 */
var MCProblemView = ProblemView.extend({
    elTemplate: '#mc-problem-template',
});

/**
 * View representing a fill-in-the-blank problem
 */
var FillProblemView = ProblemView.extend({
    elTemplate: '#fill-problem-template',
});

/**
 * View representing a fill-in-the-blank problem
 */
var TryProblemView = ProblemView.extend({
    elTemplate: '#try-problem-template',
});

/**
 * View for a collection of problems
 */
var ProblemCollectionView = Backbone.View.extend({
    problemViews: [],

    initialize: function() {
        var self = this;
        this.collection.each(function(problem) {
            // determine the appropriate view for the problem type
            var type = problem.get('type');
            var viewType = false;
            if (type == 'tf')
                viewType = TFProblemView;
            else if (type == 'mc')
                viewType = MCProblemView;
            else if (type == 'fill')
                viewType = FillProblemView;
            else if (type == 'try')
                viewType = TryProblemView;

            // make sure problem type is valid
            if (!viewType)
                return;

            // save problem-specific view
            self.problemViews.push(new viewType({
                model: problem
            }));
        });

        this.render();
    },

    render: function() {
        // add each problem view to the element
        var self = this;
        _.each(this.problemViews, function(view) {
            self.$el.append(view.el);
        });
    }
});

$(function() {
    var problemsView = new ProblemCollectionView({
        el: '#problems',
        collection: new ProblemCollection(pset)
    });
});

/**
 * View representing a single pset problem
 */
var ProblemView = Backbone.View.extend({
    el: '#problem',

    initialize: function() {
        this.problem = this.options.problem;
        this.template = Handlebars.compile($('#tf-problem-template').html());

        this.render();
    },

    render: function() {
        this.$el.html(this.template({ problem: this.problem }));
    }
});

/**
 * View representing a true/false problem
 */
var TFProblemView = ProblemView.extend({
    template: '#tf-problem-template',
});

/**
 * Router for a problem set
 */
var PsetRouter = Backbone.Router.extend({
    initialize: function() {
        this.problemIndex = 0;
    },

    routes: {
        'pset/:chapter': function(chapter) {
            this.navigate('/pset/' + chapter + '/' + this.problemIndex, { trigger: true });
        },

        'pset/:chapter/:problem': function(chapter, problem) {
            this.renderProblem(problem);
        }
    },

    /**
     * Render a problem in the main content view
     * @param {Number} problem Index of problem to render
     */
    renderProblem: function(problemIndex) {
        // remove view for previous problem
        if (this.problemView)
            this.problemView.remove();

        // add new problem in its place
        var problem = pset[problemIndex];
        if (problem.type == 'tf')
            this.problemView = new TFProblemView({
                problem: problem
            });

        // remember the current problem value
        this.problemIndex = problemIndex;
    }
});

$(function() {
    psetRouter = new PsetRouter();
    Backbone.history.start({ pushState: true });
});

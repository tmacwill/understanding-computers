/**
 * View representing a single pset problem
 */
var ProblemView = Backbone.View.extend({
    el: '#problem',

    initialize: function() {
        this.problem = this.options.problem;
        this.template = _.template($(this.elTemplate).html());

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
 * View representing controls to navigate among problems
 */
var ProblemControls = Backbone.View.extend({
    el: '#problem-controls',

    events: {
        'click #btn-next': 'next'
    },

    initialize: function() {
        // hide next button if at the last question
        var fragment = window.location.pathname.split('/');
        if (parseInt(fragment[3]) == pset.length - 1)
            this.$el.find('#btn-next').hide();
    },

    /**
     * Display the next problem
     */
    next: function() {
        // get the index of the next problem
        var fragment = Backbone.history.fragment.split('/');
        fragment[2] = parseInt(fragment[2]) + 1;

        // navigate to next problem
        psetRouter.navigate(fragment.join('/'), { trigger: true });

        // hide next button if there are no more problems
        if (fragment[2] == pset.length - 1)
            this.$el.find('#btn-next').hide();
        else
            this.$el.find('#btn-next').show();
    }
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
        // add new problem in its place
        var problem = pset[problemIndex];
        if (problem.type == 'tf')
            this.problemView = new TFProblemView({
                problem: problem,
                index: problemIndex
            });
        else if (problem.type == 'mc')
            this.problemView = new MCProblemView({
                problem: problem,
                index: problemIndex
            });
        else if (problem.type == 'fill')
            this.problemView = new FillProblemView({
                problem: problem,
                index: problemIndex
            });
        else if (problem.type == 'try')
            this.problemView = new TryProblemView({
                problem: problem,
                index: problemIndex
            });

        // remember the current problem value
        this.problemIndex = problemIndex;
    }
});

$(function() {
    var problemControls = new ProblemControls;

    psetRouter = new PsetRouter();
    Backbone.history.start({ pushState: true });
});

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

    correctTemplateId: '#correct-template',
    incorrectTemplateId: '#incorrect-template',

    events: {
        'click .btn-submit': 'checkAnswer'
    },

    initialize: function() {
        this.template = _.template($(this.elTemplate).html());
        this.correctTemplate = _.template($(this.correctTemplateId).html());
        this.incorrectTemplate = _.template($(this.incorrectTemplateId).html());

        this.render();
    },

    render: function() {
        this.$el.html(this.template({ problem: this.model }));
        return this;
    },

    /**
     * Get the currently selected answer, overriden by subclasses
     */
    answer: function() {
        return false;
    },

    /**
     * Check if the currently selected answer is correct
     */
    checkAnswer: function() {
        // send answer to server
        var answer = this.answer();
        var self = this;
        $.post('/answer/' + this.model.get('id'), { answer: answer }, function(response) {
            // display feedback on correctness
            if (response.correct)
                self.$el.find('.btn-submit').after(self.correctTemplate({ problem: self.model }));
            else
                self.$el.find('.btn-submit').after(self.incorrectTemplate({ problem: self.model }));

            // display points if any have been earned
            if (response.points)
                new NotificationView({
                    title: 'You earned ' + response.points + ' points!',
                    message: 'Awesome! More correct answers will earn you more points!'
                });
        });

        // disable submit button
        this.$el.find('.btn-submit').attr('disabled', true);
    }
});

/**
 * View representing a true/false problem
 */
var TFProblemView = ProblemView.extend({
    elTemplate: '#tf-problem-template',

    answer: function() {
        return this.$el.find('.checked input').val();
    }
});

/**
 * View representing a multiple choice problem
 */
var MCProblemView = ProblemView.extend({
    elTemplate: '#mc-problem-template',

    answer: function() {
        return this.$el.find('.checked input').val();
    }
});

/**
 * View representing a fill-in-the-blank problem
 */
var FillProblemView = ProblemView.extend({
    elTemplate: '#fill-problem-template',

    answer: function() {
        return this.$el.find('.txt-response').val()
    }
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
        // instantiate a problem model for each problem in the collection
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

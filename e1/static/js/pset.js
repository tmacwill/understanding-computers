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
                self.$el.find('.btn-next').after(self.correctTemplate({ problem: self.model }));
            else
                self.$el.find('.btn-next').after(self.incorrectTemplate({ problem: self.model }));

            // display points if any have been earned
            if (response.points) {
                if (!ProblemView.notified)
                    new NotificationView({
                        title: 'You earned ' + response.points + ' points!',
                        message: 'Awesome! More correct answers will earn you more points!'
                    });
                else
                    new NotificationView({
                        title: '+' + response.points + ' points!',
                        message: 'Awesome!',
                        timeout: 1500
                    });

                ProblemView.notified = true;
            }
        });

        // disable submit button
        this.$el.find('.btn-submit').attr('disabled', true);
    }
}, {
    notified: false,

    /**
     * Get the constructor for a problem view based on its string representation
     */
    problemViewType: function(type) {
        if (type == 'tf')
            return TFProblemView;
        else if (type == 'mc')
            return MCProblemView;
        else if (type == 'fill')
            return FillProblemView;
        else if (type == 'try')
            return TryProblemView;
        else if (type == 'sequence')
            return SequenceProblemView;

        return false;
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
 * View representing a sequence problem
 */
var SequenceProblemView = ProblemView.extend({
    problemViews: [],
    index: -1,
    elTemplate: '#sequence-problem-template',

    events: {
        'click .btn-submit': 'checkAnswer',
        'click .btn-next': 'next'
    },

    /**
     * Check the answer to one of the problems in the sequence
     */
    checkAnswer: function() {
        // show next button
        if (this.index < this.problemViews.length - 1)
            this.$el.find('.btn-next').show();

        // check answer for problem
        this.problemViews[this.index].checkAnswer();
    },

    /**
     * Go to the next question in the sequence
     */
    next: function() {
        // hide all problems
        this.$el.find('.sequence-problems .problem, .sequence-problems .btn-next').hide();

        // show the given problem
        this.index++;
        this.$el.find('.sequence-problems .problem:nth-child(' + parseInt(this.index + 1) + ')').show();
    },

    render: function() {
        this.$el.html(this.template({ problem: this.model }));

        var self = this;
        _.each(this.model.get('questions'), function(question) {
            // determine the appropriate view for the problem type
            var viewType = ProblemView.problemViewType(question.type);

            // make sure problem type is valid
            if (!viewType)
                return;

            // add view for problem
            var view = new viewType({
                model: new Problem(question)
            });
            view.undelegateEvents();
            self.$el.find('.sequence-problems').append(view.el);

            // keep track of views
            self.problemViews.push(view);
        });

        // show the first problem in the sequence
        this.next();
    }
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
            var viewType = ProblemView.problemViewType(type);

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

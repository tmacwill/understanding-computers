/**
 * Convert a subheading to an ID
 * @param {String} s Text of subheading
 * @return {String} ID representation of subheading
 */
var subheading = function(s) {
    return s.toLowerCase().replace(/ /g, '-');
};

/**
 * View representing the page's body content
 */
var ChapterView = Backbone.View.extend({
    el: '#chapter-content',
    notified: false,

    initialize: function() {
        // array of html strings for each section in the chapter
        this.sections = [];

        // iterate over each subheading to extract section text
        var self = this;
        $('#chapter-content h2').each(function() {
            // construct html string from all elements until next subheading
            var elements = $(this).nextUntil('h2');
            var html = this.outerHTML;
            $.each(elements, function() {
                html += this.outerHTML;
            });

            // save each section
            self.sections.push({
                title: $(this).html(),
                html: html
            });
        });

        // display the first section by default
        this.currentIndex = 0;
    },

    /**
     * Render a section in the body content area
     * @param {String} title Title of section to render
     */
    renderSection: function(title) {
        // mark section as read
        var fragment = Backbone.history.fragment.split('/');
        var self = this;
        $.get('/read/' + fragment[1] + '/' + fragment[2], function(response) {
            // if we haven't read this section yet, then display notification
            if (response.points) {
                if (!self.notified)
                    new NotificationView({
                        title: 'You earned ' + response.points + ' points!',
                        message: 'Nice job! You\'ll earn points for each section you read. Keep going!'
                    });
                else
                    new NotificationView({
                        title: '+' + response.points + ' points!',
                        message: 'Nice!',
                        timeout: 1500
                    });

                self.notified = true;
            }
        });

        // search for section matching the given title
        for (var i in this.sections) {
            if (subheading(this.sections[i].title) == title) {
                // scroll to the top of the page
                window.scrollTo(0, 0);

                // render section at new index
                this.currentIndex = i;
                this.$el.html(this.sections[i].html);
                break;
            }
        }
    }
});

/**
 * View representing the drop-down table of contents
 */
var ChapterMenuView = Backbone.View.extend({
    initialize: function() {
        this.template = _.template($('#chapter-menu-template').html());
        $('#navbar #subtitle').html($('#navbar #subtitle').html() + '<i class="icon-angle-down"></i>');

        this.render();
    },

    render: function() {
        this.$el.html(this.template());
        $('#navbar #title').after(this.$el);
    }
});

/**
 * View representing a marker that can be used to change sections
 */
var SectionSelectorView = Backbone.View.extend({
    el: '#section-selectors',

    events: {
        'click li a.btn-section': 'renderSection',
        'click li.previous a': 'previous',
        'click li.next a': 'next'
    },

    initialize: function() {
        // compile template for view
        this.chapterView = this.options.chapterView;
        this.template = _.template($('#section-selector-template').html());

        this.render();

        // enable tooltips on all selectors
        this.$el.find('[data-toggle=tooltip]').tooltip();
    },

    render: function() {
        this.$el.html(this.template({
            sections: this.chapterView.sections
        }));

        return this;
    },

    /**
     * Set the currently active section in the selector
     */
    highlightSection: function(title) {
        this.$el.find('.active').removeClass('active');
        this.$el.find('[data-id="' + subheading(title) + '"]').parent().addClass('active');
    },

    /**
     * Render the next section
     */
    next: function() {
        // check if we should go to a section
        if (this.chapterView.currentIndex < this.chapterView.sections.length - 1) {
            // determine which section to navigate to
            var fragment = Backbone.history.fragment.split('/');
            fragment[2] = subheading(this.chapterView.sections[parseInt(this.chapterView.currentIndex) + 1].title);

            // navigate to section
            chapterRouter.navigate(fragment.join('/'), { trigger: true });
        }

        // on last section, go to pset
        else
            window.location.href = $('#btn-pset').attr('href');
    },

    /**
     * Render the previous section
     */
    previous: function() {
        // check if we should go to a section
        if (this.chapterView.currentIndex > 0) {
            // determine which section to navigate to
            var fragment = Backbone.history.fragment.split('/');
            fragment[2] = subheading(this.chapterView.sections[parseInt(this.chapterView.currentIndex) - 1].title);

            // navigate to section
            chapterRouter.navigate(fragment.join('/'), { trigger: true });
        }

        // on first section, go to table of contents
        else
            window.location.href = $('#btn-contents').attr('href');
    },

    /**
     * Render the selected section
     */
    renderSection: function(e) {
        // determine which section to navigate to
        var fragment = Backbone.history.fragment.split('/');
        fragment[2] = subheading($(e.target).attr('data-original-title'));

        // navigate to section
        chapterRouter.navigate(fragment.join('/'), { trigger: true });
    }
});

/**
 * Router for chapter page
 */
var ChapterRouter = Backbone.Router.extend({
    initialize: function(options) {
        this.chapterView = options.chapterView;
        this.sectionSelectorView = options.sectionSelectorView;
    },

    routes: {
        // if no section given, then redirect to first section in the chapter
        'chapter/:chapter': function(chapter) {
            var first = this.chapterView.sections[0];
            this.navigate('chapter/' + chapter + '/' + subheading(first.title), { trigger: true });
        },

        // display the given section in the chapter
        'chapter/:chapter/:section': function(chapter, section) {
            this.chapterView.renderSection(section);
            this.sectionSelectorView.highlightSection(section);
        }
    }
});

$(function() {
    // create views for main body content and section selection
    var chapterMenuView = new ChapterMenuView;
    var chapterView = new ChapterView;
    var sectionSelectorView = new SectionSelectorView({
        chapterView: chapterView
    });

    // create router
    chapterRouter = new ChapterRouter({
        chapterView: chapterView,
        sectionSelectorView: sectionSelectorView
    });

    Backbone.history.start({ pushState: true });
});

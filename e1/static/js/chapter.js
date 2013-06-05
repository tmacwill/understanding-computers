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

    initialize: function() {
        // array of html strings for each section in the chapter
        this.sections = [];

        // get all of the html from the start of the document until the first subheading
        var html = this.$el.children()[0].outerHTML;
        var elements = this.$el.children().eq(0).nextUntil('h2');
        $.each(elements, function() {
            html += this.outerHTML;
        });

        // use that html to create the first section
        this.sections.push({
            title: $('h1 small').html(),
            html: html
        });

        // iterate over each subheading to extract section text
        var self = this;
        $('h2').each(function() {
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
        // if current url has no section component, then convert title to section and use that
        var fragment = window.location.pathname.split('/');
        var n = fragment.length;
        if (n < 4)
            fragment[3] = subheading(title);

        // mark section as read
        $.get('/read/' + fragment[2] + '/' + fragment[3], function(response) {
            // if we haven't read this section yet, then display notification
            if (response.points) {
                new NotificationView({
                    title: 'You earned ' + response.points + ' points!',
                    message: 'Nice job! You\'ll earn points for each section you read. Keep going!'
                });
            }
        });

        // search for section matching the given title
        for (var i in this.sections) {
            // if no subsection given, then use first subsection, else look for matching title
            if (subheading(this.sections[i].title) == title || n < 4) {
                // scroll to the top of the page
                window.scrollTo(0, 0);

                // render section at new index
                this.currentIndex = i;
                this.$el.html(this.sections[i].html);
                return;
            }
        }
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
        // if no section given, then display the first section in the chapter
        'chapter/:chapter': function(chapter) {
            var first = this.chapterView.sections[0];
            this.chapterView.renderSection(first.title);
            this.sectionSelectorView.highlightSection(first.title);
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
    var chapterView = new ChapterView();
    var sectionSelectorView = new SectionSelectorView({
        chapterView: chapterView
    });

    // create router
    chapterRouter = new ChapterRouter({
        chapterView: chapterView,
        sectionSelectorView: sectionSelectorView
    });

    // menu on left side
    $('#chapters-menu').width(($(window).width() - $('.container').width() - 20) / 2);
    $('#chapters-menu').hover(function() {
        $('#chapters-menu-list').slideDown('fast');
    }, function() {
        $('#chapters-menu-list').slideUp('fast');
    });

    Backbone.history.start({ pushState: true });
});

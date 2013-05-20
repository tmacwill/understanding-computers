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
        this.$el.html(this.sections[0].html);
    },

    /**
     * Render a section in the body content area
     * @param {String} index ID of section to render
     */
    renderSection: function(index) {
        this.$el.html(this.sections[index].html);
    }
});

/**
 * View representing a marker that can be used to change sections
 */
var SectionSelectorView = Backbone.View.extend({
    el: '#section-selectors',

    events: {
        'click .section-selector': 'renderSection'
    },

    initialize: function() {
        // compile template for view
        this.chapterView = this.options.chapterView;
        this.template = Handlebars.compile($('#section-selector-template').html());

        // construct a selector for each page
        var self = this;
        $.each(this.chapterView.sections, function(i, e) {
            self.$el.append(self.template({
                title: this.title
            }));
        });

        // enable tooltips on all selectors
        this.$el.children().tooltip();
    },

    renderSection: function(e) {
        // scroll to the top of the page
        window.scrollTo(0, 0);

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
    },

    routes: {
        'chapter/:chapter/:section': function(chapter, section) {
            var self = this;
            $.each(this.chapterView.sections, function(i, e) {
                if (subheading(this.title) == section)
                    self.chapterView.renderSection(i);
            });
        }
    }
});

$(function() {
    // enable table of contents on sidebar
    $('#toggle-menu').sidr();

    // create views for main body content and section selection
    var chapterView = new ChapterView();
    var sectionSelectorView = new SectionSelectorView({
        chapterView: chapterView
    });

    // create router
    chapterRouter = new ChapterRouter({
        chapterView: chapterView
    });

    Backbone.history.start({ pushState: true });
});

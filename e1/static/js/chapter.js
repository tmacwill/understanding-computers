var ChapterView = Backbone.View.extend({
    el: '#chapter-content',

    initialize: function() {
        this.sections = [];
        var html = this.$el.children()[0].outerHTML;
        var elements = this.$el.children().eq(0).nextUntil('h2');
        $.each(elements, function() {
            html += this.outerHTML;
        });
        this.sections.push({
            title: $('h1 small').html(),
            html: html
        });

        var self = this;
        $('h2').each(function() {
            var elements = $(this).nextUntil('h2');
            var html = this.outerHTML;

            $.each(elements, function() {
                html += this.outerHTML;
            });

            self.sections.push({
                title: $(this).html(),
                html: html
            });
        });

        this.$el.html(this.sections[0].html);
    },

    renderSection: function(index) {
        this.$el.html(this.sections[index].html);
    }
});

var SectionSelectorView = Backbone.View.extend({
    el: '#section-selectors',

    events: {
        'click .section-selector': 'renderSection'
    },

    initialize: function() {
        this.chapterView = this.options.chapterView;
        this.template = Handlebars.compile($('#section-selector-template').html());

        var self = this;
        $.each(this.chapterView.sections, function(i, e) {
            self.$el.append(self.template({
                title: this.title
            }));
        });

        this.$el.children().tooltip();
    },

    renderSection: function(e) {
        window.scrollTo(0, 0);
        var fragment = Backbone.history.fragment.split('/');
        fragment[2] = $(e.target).attr('data-original-title').toLowerCase().replace(/ /g, '-');
        chapterRouter.navigate(fragment.join('/'), { trigger: true });
    }
});

var ChapterRouter = Backbone.Router.extend({
    routes: {
        'chapter/:chapter/:section': function(chapter, section) {
            $.each(chapterView.sections, function(i, e) {
                if (this.title.toLowerCase().replace(/ /g, '-') == section)
                    chapterView.renderSection(i);
            });
        }
    }
});

$(function() {
    // enable table of contents on sidebar
    $('#toggle-menu').sidr();

    chapterView = new ChapterView();
    sectionSelectorView = new SectionSelectorView({
        chapterView: chapterView
    });

    chapterRouter = new ChapterRouter();
    Backbone.history.start({ pushState: true });
});

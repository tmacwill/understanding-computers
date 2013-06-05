/**
 * View representing a notification
 */
var NotificationView = Backbone.View.extend({
    events: {
        'click': 'hide'
    },

    initialize: function() {
        this.title = this.options.title;
        this.message = this.options.message;
        this.template = _.template($('#notification-template').html());

        this.render();
    },

    render: function() {
        this.$el.html(this.template({
            title: this.title,
            message: this.message
        }));

        this.$el.hide();
        $('body').append(this.$el);

        var self = this;
        setTimeout(function() {
            self.$el.fadeIn('fast');
        }, 300);

        // hide after 4 sections
        setTimeout(function() {
            self.hide();
        }, 4000);
    },

    hide: function() {
        var self = this;
        this.$el.fadeOut('fast', function() {
            self.$el.remove();
        });
    }
});

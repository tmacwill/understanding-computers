$(function() {
    var height = window.innerHeight - $('h1').outerHeight(true);
    $('#table-contents').height(height);
    $('#table-contents').width(window.innerWidth - $('#table-contents').position().left);

    stroll.bind('#table-contents');
});

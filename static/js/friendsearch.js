// filepath: /c:/Users/Pgcke/Documents/visual studio projects/gifting-genie-two/static/js/friendsearch.js
$(document).ready(function() {
    $('#search-button').on('click', function() {
        var query = $('#search_query').val();
        if (query.length > 2) {
            $.ajax({
                url: searchUsernamesUrl,
                data: {
                    'term': query
                },
                dataType: 'json',
                success: function(data) {
                    var suggestions = data.map(function(username) {
                        return '<option value="' + username + '">';
                    });
                    $('#username-suggestions').html(suggestions.join(''));
                    if (data.length > 0) {
                        $('#id_friend_username').val(data[0]);
                    }
                }
            });
        }
    });
});
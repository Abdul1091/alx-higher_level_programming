$(document).ready(function() {
  // Make an AJAX GET request to the URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Set the text of the div with id hello to the value of hello from the response
    $('#hello').text(data.hello);
  });
});

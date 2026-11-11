$(document).ready(function () {
    $('#dataForm').submit(function (event) {
        event.preventDefault(); // Prevent form from submitting normally

        // Gather data from the form
        var formData = {
            data1: document.getElementById("data1").value,
            data2: document.getElementById("data2").value
        };
		
		document.getElementById("data1").value = "";
		document.getElementById("data2").value = "";

        // Send data to the server via AJAX
        $.ajax({
            type: 'POST',
            url: '/submit',
            data: formData,
            success: function (response) {
                // Display success message
                $('#response').html('Response: ' + response.message);

                // Clear existing rows in the table body
                $('table tbody').empty();

                // Append new rows based on the updated data from the server
                response.data.forEach(function (row) {
                    $('table tbody').append('<tr><td>' + row[0] + '</td><td>' + row[1] + '</td></tr>');
                });
            },
            error: function (error) {
                $('#response').html('Error: ' + error.responseText);
            }
        });
    });
});


function calculateHealth() {
    var data = {
        "push_up": document.getElementById('push_up').value,
        "pull_up": document.getElementById('pull_up').value,
        "squat": document.getElementById('squat').value,
        "fivekm_time": document.getElementById('fivekm_time').value,
        "crunches": document.getElementById('crunches').value
    };
    fetch('/calculate_health', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const table = document.createElement('table');
        table.border = '1';

        const headers = ['Overall Score', 'Push Up Level', 'Pull Up Level', 'Squat Level', '5k Level', 'Crunches Level'];
        
        // Create table header
        const headerRow = document.createElement('tr');
        for (const header of headers) {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        }
        table.appendChild(headerRow);

        // Create table body
        const dataRow = document.createElement('tr');
        dataRow.innerHTML = `
            <td>${result.overall_score}</td>
            <td>${result.push_up_norm}</td>
            <td>${result.pull_up_norm}</td>
            <td>${result.squat_norm}</td>
            <td>${result.fivekm_time_norm}</td>
            <td>${result.crunches_norm}</td>
        `;
        table.appendChild(dataRow);

        // Append the table to the 'result' element
        document.getElementById('result').appendChild(table);
    });

}
function addToDatabase(){
    var data = {
        "push_up": document.getElementById('push_up').value,
        "pull_up": document.getElementById('pull_up').value,
        "squat": document.getElementById('squat').value,
        "fivekm_time": document.getElementById('fivekm_time').value,
        "crunches": document.getElementById('crunches').value
    };
    // A fetch request is made to the server endpoint "/add_to_data" using the POST method
    fetch('/add_to_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
    // Check if the server responded with success
    if (result.success) {
        // Display a success message on the website
        document.getElementById('result').innerHTML = '<p>Database successfully updated!</p>';
    } else {
        // Display an error message if the server response indicates failure
        document.getElementById('result').innerHTML = '<p>Error updating the database.</p>';
    }
})
.catch(error => {
    console.error('Error:', error);
    // Display an error message in case of a fetch error
    document.getElementById('result').innerHTML = '<p>Error updating the database.</p>';
});
}
function clearResults() {
    // JavaScript function to clear results
    document.getElementById('result').innerHTML = '';
}

function displayDatabase(){

    // A fetch request is made to the server endpoint "/" using the POST method
    fetch('/display_database', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        // Clear previous results
        document.getElementById('result').innerHTML = '';
        // Create a table for each record
        const table = document.createElement('table');
        table.border = '1';

        const headers = ['Overall Score', 'Push Up Level', 'Pull Up Level', 'Squat Level', '5k Level', 'Crunches Level'];
        // Create table header
        const headerRow = document.createElement('tr');
        for (const header of headers) {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        }
        table.appendChild(headerRow);

        result.forEach(result => {
            // Create table body
            const dataRow = document.createElement('tr');
            dataRow.innerHTML = `
                <td>${result.overall_score}</td>
                <td>${result.push_up_norm}</td>
                <td>${result.pull_up_norm}</td>
                <td>${result.squat_norm}</td>
                <td>${result.fivekm_time_norm}</td>
                <td>${result.crunches_norm}</td>
            `;
            table.appendChild(dataRow);

            // Append the table to the 'result' element
            document.getElementById('result').appendChild(table);
        });

    })
}
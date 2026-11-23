// Lists to store the data
let days = [];
let hours = [];
let schoolDays = [];

// Run this code when the form is submitted
document.getElementById("dataForm").addEventListener("submit", function (event) {
  event.preventDefault();   // stop the page from reloading

  // Read the values from the form
  let day = document.getElementById("dayInput").value;
  let hrs = Number(document.getElementById("hoursInput").value);
  let isSchoolDay = document.getElementById("schoolDay").checked;

  // Store them in the lists
  days.push(day);
  hours.push(hrs);
  schoolDays.push(isSchoolDay);

  drawGraph();     // update the graph
  this.reset();    // clear the form for the next entry
});

function drawGraph() {
  // Choose a colour for each bar using a loop and a condition
  let colours = [];
  for (let i = 0; i < schoolDays.length; i++) {
    if (schoolDays[i] === true) {
      colours.push("royalblue");
    } else {
      colours.push("orange");
    }
  }

  // The data: one trace
  let trace = {
    x: days,
    y: hours,
    type: "bar",
    marker: { color: colours }
  };

  // The layout: title and axis labels
  let layout = {
    title: "Daily Screen Time (blue = school day, orange = not)",
    xaxis: { title: "Day" },
    yaxis: { title: "Hours" }
  };

  // Draw it in the div with id="graph"
  Plotly.newPlot("graph", [trace], layout);
}

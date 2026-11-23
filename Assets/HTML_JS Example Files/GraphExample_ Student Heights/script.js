let heightsList = [];   //create empty list
let heightEle = document.getElementById("heightIn"); 

function addData() {
	heightsList.push(heightEle.value);  //add height to list
	drawPlotly();        //call function to draw graph
	heightEle.value = "";  //clear input box
}

function drawPlotly() {    
	let heights = {
		y: heightsList,
		name: "Height",
		mode: "lines+markers"
	};
	
	let layout = {
		title: "Students heights",
		xaxis: {title:"Student"},
		yaxis: {title: "height (m)"}
	};
	
	let data=[heights]
	Plotly.newPlot("graph",data,layout);   //draw graph
}
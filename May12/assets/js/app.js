// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.
var svgWidth = 480;
var svgHeight = 330;


var chartMargin = {
  top: 20,
  right: 20,
  bottom: 20,
  left: 20
};


var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;


var svg = d3
  .select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth)

var graphs = svg.append('g')
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

var points = [];

d3.csv('assets/data/MHI_angina.csv',function(error, data) {
    if(error){console.warn(error)}
    var xScale = d3.scaleLinear()
        .domain([0,d3.max(data.map(x=>x.MHI))])
        .range([0, chartWidth]);

    var yScale = d3.scaleLinear()
        .domain([0,d3.max(data.map(x=>x.Data_value))])
        .range([chartHeight,0]);

    var yAxis = d3.axisLeft(yScale);
    var xAxis = d3.axisBottom(xScale);

    graphs.append('g')
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(xAxis);
    
    graphs.append('g')
        .call(yAxis)

    for(elem in data) {
        let item = data[elem];
       
        points.push({'x_axis':item.MHI,'y_axis':item.Data_value,'radius':20})
        
    }
    // console.log(points)
    var circles = graphs.selectAll('circle')
        .data(points)
        .enter()
        .append('circle');

    var circleAttributes = circles
        .attr("cx", x=>xScale[x.x_axis])
        .attr("cy", x=>yScale[x.y_axis])
        .attr("r", function (d) { return d.radius; })
        .style("fill", function(d) { return d.color; });
})
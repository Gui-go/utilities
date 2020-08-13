// Seasonal Boxplot of inflation in Brazil from 2000 to 2020.5

// set the dimensions and margins of the graph
var margin = { top: 10, right: 30, bottom: 50, left: 40 },
    width = 860 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("./ipca2.csv").then(function (data) {

    // Compute stats
    var stat = d3.nest() // Factoring data
        .key(function (d) { return d.months; })
        .rollup(function (d) {
            q1 = d3.quantile(d.map(function (d) { return d.ipca; }).sort(d3.ascending), .25)
            median = d3.quantile(d.map(function (d) { return d.ipca; }).sort(d3.ascending), .5)
            q3 = d3.quantile(d.map(function (d) { return d.ipca; }).sort(d3.ascending), .75)
            interQuantileRange = q3 - q1
            min = q1 - 1.5 * interQuantileRange
            max = q3 + 1.5 * interQuantileRange
            return ({ q1: q1, median: median, q3: q3, interQuantileRange: interQuantileRange, min: min, max: max })
        })
        .entries(data);
    var uniqueM = Array.from({ length: stat.length }, (x, i) => i + 1)

    // X scale
    var x = d3.scaleBand()
        .range([0, width])
        .domain(uniqueM)
        .paddingInner(1)
        .paddingOuter(.5)
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .style("font-size", "18px")

    // Y scale
    var y = d3.scaleLinear()
        .domain([-0.8, 1.6])
        .range([height, 0])
    svg.append("g")
        .call(d3.axisLeft(y))
        .style("font-size", "18px")

    // Main vertical line
    svg
        .selectAll("vertLines")
        .data(stat)
        .enter()
        .append("line")
        .attr("x1", function (d) { return (x(d.key)) })
        .attr("x2", function (d) { return (x(d.key)) })
        .attr("y1", function (d) { return (y(d.value.min)) })
        .attr("y2", function (d) { return (y(d.value.max)) })
        .attr("stroke-width", "2")
        .attr("stroke", "black")

    // rectangle for the main box
    var boxWidth = 33
    svg
        .selectAll("boxes")
        .data(stat)
        .enter()
        .append("rect")
        .attr("x", function (d) { return (x(d.key) - boxWidth / 2) })
        .attr("y", function (d) { return (y(d.value.q3)) })
        .attr("height", function (d) { return (y(d.value.q1) - y(d.value.q3)) })
        .attr("width", boxWidth)
        .attr("stroke-width", "1")
        .attr("stroke", "black")
        .style("fill", "#009502")

    // Show the median
    svg
        .selectAll("medianLines")
        .data(stat)
        .enter()
        .append("line")
        .attr("x1", function (d) { return (x(d.key) - boxWidth / 2) })
        .attr("x2", function (d) { return (x(d.key) + boxWidth / 2) })
        .attr("y1", function (d) { return (y(d.value.median)) })
        .attr("y2", function (d) { return (y(d.value.median)) })
        .attr("stroke-width", "3")
        .attr("stroke", "black")

    // create a tooltip
    var Tooltip = d3.select("#chart")
        .append("div")
        .style("opacity", 0)
        .style("background-color", "#000")
        .style("color", "#FFF")
        .style("text-align", "center")
        .style("border", "solid")
        .style("border-width", "2px")
        .style("border-radius", "5px")
        .style("padding", "5px")
        .style("max-width", "820px")

    // Tooltip
    var mouseover = function (d) {
        Tooltip
            .style("opacity", 1)
        d3.select(this)
            .style("stroke", "black")
            .style("opacity", 1)
    }
    var mousemove = function (d) {
        Tooltip
            .html(`Inflação mensal de  ${d.ipca}% correspondente ao mês: ${d.date}`)
            .style("left", (d3.mouse(this)[0]) + "px")
            .style("top", (d3.mouse(this)[1]) + "px")
    }
    var mouseleave = function (d) {
        Tooltip
        d3.select(this)
            .style("fill", "gray")
            .style("stroke", "#000")
            .style("opacity", 0.6)
    }

    // Points with jitter
    var jitterWidth = 5
    svg
        .selectAll("Points")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return (x(d.months) - jitterWidth / 2 + Math.random() * jitterWidth) })
        .attr("cy", function (d) { return (y(d.ipca)) })
        .attr("r", 4)
        .style("fill", "gray")
        .style("opacity", .6)
        .attr("stroke", "#000")
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)

    // Show the mean line
    svg
        .selectAll("meanLines")
        .data(stat)
        .enter()
        .append("line")
        .attr("x1", function (d) { return (x(1)) })
        .attr("x2", function (d) { return (x(12)) })
        .attr("y1", y(data[0].mean))
        .attr("y2", y(data[0].mean))
        .attr("stroke-width", "3")
        .attr("stroke", "red")

    // Show the median line
    svg
        .selectAll("medianLines")
        .data(stat)
        .enter()
        .append("line")
        .attr("x1", function (d) { return (x(1)) })
        .attr("x2", function (d) { return (x(12)) })
        .attr("y1", y(data[0].median))
        .attr("y2", y(data[0].median))
        .attr("stroke-width", "3")
        .attr("stroke", "blue")


})
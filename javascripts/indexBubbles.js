var diameter = 500,
    format = d3.format(",d"),
    dataSource = 0,
   // color = d3.scale.category20(),
    attrCount = 0;

var selectedAttributes = [];

var pack = d3.layout.pack()
    .size([diameter - 4, diameter - 4])
    .sort( function(a, b) {
        return -(a.value - b.value);
    })
    .value(function(d) { return d.size; });

var svg = d3.select("#indexBubbles").append("svg")
    .attr("width", diameter)
    .attr("height", diameter);

var data = getData();

var vis = svg.datum(data).selectAll(".node")
    .data(pack.nodes)
    .enter()
    .append("g")
    .on("click", function(d) { if (d.name != "Root") updateVis(d);});


var circles = vis.append("circle")
    .style("fill", function(d, i) { if (d.name == "Root") return "beige"; else return "#bdbdbd"; })
    .attr("cx", function(d) { return d.x; })
    .attr("cy", function(d) { return d.y; })
    .attr("r", function(d) { return d.r; });


var circleTexts = vis.append("text")
    .attr("dy", ".3em")
    .attr("x", function(d) { return d.x; })
    .attr("y", function(d) { return d.y; })
    .style("text-anchor", "middle")
    .text(function(d) {  if (d.name == "Root") return ""; else return d.name });

//updateVis();

function updateVis(d) {

    pack.value(function(xd) { return getSize(xd, d.name)});

    var data1 = pack.nodes(data);

    circles.transition()
        .duration(1500)
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("r", function(d) { return d.r})
        .style("fill", function (xD) { if (d.name == xD.name || selectedAttributes.indexOf(xD.name.toLowerCase()) >= 0) return "#62CC8E"; else  if (xD.name == "Root") return "beige"; else return "#bdbdbd";})
        .each('end',function(xD){if (attrCount == 5) { if (xD.name == d.name) window.open("dataViz.html?attributes="+selectedAttributes, "_self");}});

    circleTexts.transition()
        .duration(1500)
        .attr("x", function(d) { return d.x; })
        .attr("y", function(d) { return d.y; });


};

function getSize(xd, name) {
    // Selected node
    if (xd.name == name) {
        var index = selectedAttributes.indexOf(xd.name.toLowerCase());

        if (index == -1) {
            selectedAttributes.push(xd.name.toLowerCase());
            attrCount++;
            return xd.size * 3;
        } else {
            selectedAttributes.splice(index, 1);
            attrCount--;
            return xd.size;
        }
    } else {
        var index = selectedAttributes.indexOf(xd.name.toLowerCase());

        if (index == -1) {
            return xd.size;
        } else {
            return xd.size * 3;
        }

    }
}

function getData() {
    return {
        "name": "Root",
        "children": [
            {"name":"Accurate", "size":500},
            {"name":"Ambience", "size":500},
            {"name":"Bake", "size":500},
            {"name":"Best", "size":500},
            {"name":"Commitment", "size":500},
            {"name":"Confidence", "size":500},
            {"name":"Delivery", "size":500},
            {"name":"Different", "size":500},
            {"name":"Economy", "size":500},
            {"name":"Enormous", "size":500},
            {"name":"Excellent", "size":500},
            {"name":"Fantastic", "size":500},
            {"name":"Filling", "size":500},
            {"name":"Flavor", "size":500},
            {"name":"Fresh", "size":500},
            {"name":"Friendly", "size":500},
            {"name":"Grow", "size":500},
            {"name":"Happy", "size":500},
            {"name":"Honest", "size":500},
            {"name":"Hot", "size":500},
            {"name":"Love", "size":500},
            {"name":"Memorable", "size":500},
            {"name":"Neighborhood", "size":500},
            {"name":"New", "size":500},
            {"name":"Pleasant", "size":500},
            {"name":"Price", "size":500},
            {"name":"Quality", "size":500},
            {"name":"Quick", "size":500},
            {"name":"Reasonable", "size":500},
            {"name":"Recommend", "size":500},
            {"name":"Service", "size":500},
            {"name":"Special", "size":500},
            {"name":"Stuff", "size":500},
            {"name":"Sturdy", "size":500},
            {"name":"Surprise", "size":500},
            {"name":"Taste", "size":500},
            {"name":"Together", "size":500},
            {"name":"Worth", "size":500},
        ]

    };
}


  
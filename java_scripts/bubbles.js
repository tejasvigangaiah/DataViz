/**
 * Created by kpbhatt on 4/4/2015.
 */
var width = document.getElementById('viz').offsetWidth-30, height = 640;
var chosenCount = 0;
 svg = d3.select('#viz')
    .append('svg')
    .attr("width", width)
    .attr("height", height);

var borderPath = svg.append("rect").attr("x", 0).attr("y", 0).attr("height", height).attr("width", width).style("stroke", "black").style("fill", "none").style("stroke-width", 1);
var splitLine = svg.append("line").attr("x1",0).attr("y1",150).attr("x2",width).attr("y2",150).style("stroke", "black").style("stroke-width", 1);

function dragstart(d) {
    console.log("NODE ===> " + d.label)
    if(Number(d3.select(this).attr("cy")) > 150){
        chosenCount--;
    }
}
function dragmove(d) {
    var movement_x = Number(d3.select(this).attr("cx")) + d3.event.dx;
    var movement_y = Number(d3.select(this).attr("cy")) + d3.event.dy;
    if(movement_x < width-20 && movement_x > 20) {
        d3.select(this).attr("cx", movement_x);
    }
    if(movement_y < height-20 && movement_y > 20) {
        d3.select(this).attr("cy", movement_y);
    }
}
function dragend(d) {

    if(Number(d3.select(this).attr("cy")) < 150) {
        d3.select(this).transition().attr("cx", 70*(d.id % 10 +1)).attr("cy", 70*(Math.floor(d.id / 10)) + 40).duration(1500);
        removeElementFrmVenSet(d);
    } else {
        chosenCount++;
        //alert(chosenCount);
        d3.select(this).transition().attr("cx", width/2).attr("cy", (height + 150)/2).duration(1500);
        addElementToVenSet(d);
    }
    d3.select("#count").html(chosenCount+ "");

}

var drag = d3.behavior.drag()
    .on("drag", dragmove)
    .on("dragstart", dragstart)
    .on("dragend", dragend);

d3.json('Data/miserables.json', function(err, data) {

    data.nodes.forEach(function(d, i) {
        d.id = i;
    });


    node = svg.selectAll('.node')
        .data( data.nodes )
        .enter().append('g')
        .attr('title', name)
        .attr('class', 'node');

    node.append('circle')
        .attr('r', 30)
        .attr('fill-opacity', 0.5)
        .attr('cx',function(d) { return 70*(d.id % 10 +1)})
        .attr('cy',function(d) { return 70*(Math.floor(d.id / 10)) + 40})
        .call(drag);

});

var combine = function(a, min) {
    var fn = function(n, src, got, all) {
        if (n == 0) {
            if (got.length > 0) {
                all[all.length] = got;
            }
            return;
        }
        for (var j = 0; j < src.length; j++) {
            fn(n - 1, src.slice(j + 1), got.concat([src[j]]), all);
        }
        return;
    }
    var all = [];
    for (var i = min; i < a.length; i++) {
        fn(i, a, [], all);
    }
    all.push(a);
    return all;
}

function removeElementFrmVenSet(info) {
    var localSets=[];
    for (var i = 0; i < sets.length; i++) {
        var index = sets[i].sets.indexOf(info.sets[0]);
        console.log("=====> REMOVE INDEX = " + index);
        if (index < 0)
            localSets.push(sets[i]);
    }
    sets = localSets;
    for (var i = 0; i < sets.length; i++) {
        console.log(sets[i]);
    }
    startDrawingVenn();
}



function addElementToVenSet(info) {
    // First element in the sets.
    sets.push({sets: info.sets, label: info.label, size: 5000});

    var localArray=[];
    for (var i = 0; i < sets.length; i++) {
        if (sets[i].label) {
            localArray.push(sets[i].sets[0]);
        }
    }

    var localCombo = combine(localArray, 2);
    console.log("============> " + JSON.stringify(localCombo));

   for (var i = 0; i < localCombo.length; i++) {
       if (localCombo[i].length > 1)
        sets.push({sets: localCombo[i], size:1000});
    }

    for (var i = 0; i < sets.length; i++) {
        console.log(sets[i]);
    }
    startDrawingVenn();
}
